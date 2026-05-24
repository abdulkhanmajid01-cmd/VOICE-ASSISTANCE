"""
Speech Engine Module
Handles speech recognition and text-to-speech functionality
"""

import speech_recognition as sr
import pyttsx3
import logging
import threading
import queue
from config import (
    LANGUAGE, TTS_RATE, TTS_VOLUME, TTS_VOICE_ID,
    SPEECH_TIMEOUT, LISTEN_TIMEOUT, DEBUG_MODE,
    MIC_INDEX, ENERGY_THRESHOLD, DYNAMIC_ENERGY_THRESHOLD, AMBIENT_NOISE_DURATION
)

# Configure logging
logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


class SpeechEngine:
    """
    Unified speech recognition and text-to-speech engine.
    Handles all audio input/output operations.
    """
    
    def __init__(self):
        """Initialize speech recognition and text-to-speech engines."""
        try:
            # Initialize speech recognizer using configuration values
            self.recognizer = sr.Recognizer()
            # Set initial energy threshold from config
            try:
                self.recognizer.energy_threshold = int(ENERGY_THRESHOLD)
            except Exception:
                self.recognizer.energy_threshold = 2000

            # Dynamic energy threshold from config
            try:
                self.recognizer.dynamic_energy_threshold = bool(DYNAMIC_ENERGY_THRESHOLD)
            except Exception:
                self.recognizer.dynamic_energy_threshold = True

            # Track whether ambient noise has been calibrated once
            self.noise_calibrated = False
            
            # Initialize text-to-speech engine
            self.tts_engine = pyttsx3.init()
            self._configure_tts()
            
            # Thread synchronization for TTS
            self.tts_active = True  # Set BEFORE starting thread
            self.tts_lock = threading.Lock()
            self.tts_queue = queue.Queue()
            self.tts_worker_thread = threading.Thread(target=self._tts_worker, daemon=False)
            self.tts_worker_thread.start()
            
            logger.info("Speech Engine initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Speech Engine: {e}")
            raise
    
    def _configure_tts(self):
        """Configure text-to-speech engine settings."""
        try:
            # Set speech rate
            self.tts_engine.setProperty('rate', TTS_RATE)
            
            # Set volume
            self.tts_engine.setProperty('volume', TTS_VOLUME)
            
            # Set voice
            voices = self.tts_engine.getProperty('voices')
            if len(voices) > TTS_VOICE_ID:
                self.tts_engine.setProperty('voice', voices[TTS_VOICE_ID].id)
            
            logger.debug("TTS engine configured")
        except Exception as e:
            logger.warning(f"Error configuring TTS: {e}")
    
    def listen(self, timeout=SPEECH_TIMEOUT):
        """
        Listen to user voice input with advanced noise filtering and error handling.
        
        Args:
            timeout (int): Maximum time to listen in seconds
            
        Returns:
            str: Recognized text from speech, or empty string if failed
        """
        try:
            # Select microphone device if configured
            mic_kwargs = {}
            if MIC_INDEX is not None:
                try:
                    mic_kwargs['device_index'] = int(MIC_INDEX)
                except Exception:
                    logger.warning(f"Invalid MIC_INDEX in config: {MIC_INDEX}")

            # Open microphone with optional device index
            try:
                with sr.Microphone(**mic_kwargs) as source:
                    logger.debug("Listening for audio input...")

                    # Ambient noise adjustment using config only once for faster repeats
                    try:
                        duration = float(AMBIENT_NOISE_DURATION)
                    except Exception:
                        duration = 0.5
                    if not self.noise_calibrated:
                        self.recognizer.adjust_for_ambient_noise(source, duration=duration)
                        self.noise_calibrated = True

                    # Optionally update energy threshold (keep from recognizer unless config overrides)
                    try:
                        self.recognizer.energy_threshold = int(ENERGY_THRESHOLD)
                    except Exception:
                        pass

                    # Listen with timeout handling
                    try:
                        audio = self.recognizer.listen(
                            source,
                            timeout=LISTEN_TIMEOUT if LISTEN_TIMEOUT else 3,
                            phrase_time_limit=timeout
                        )
                    except sr.WaitTimeoutError:
                        logger.debug("Listening timeout - no speech detected")
                        return ""

                # Recognize speech using Google Speech Recognition
                try:
                    text = self.recognizer.recognize_google(audio, language=LANGUAGE)
                    logger.info(f"Recognized: {text}")
                    return text.lower()
                except sr.UnknownValueError:
                    logger.debug("Could not understand audio")
                    return ""
                except sr.RequestError as e:
                    logger.error(f"Google Speech Recognition error: {e}")
                    return ""

            except OSError as e:
                logger.error(f"Microphone not found or not available: {e}")
                logger.debug("Possible fixes: Check microphone connection, set MIC_INDEX in config.py")
                return ""

        except Exception as e:
            logger.error(f"Unexpected error during listening: {e}")
            return ""
    
    def speak(self, text):
        """
        Convert text to speech and play it.
        Queue the text for processing by the TTS worker thread.
        
        Args:
            text (str): Text to be spoken
        """
        try:
            if not self.tts_active:
                logger.warning("TTS engine is not active")
                return
            
            logger.debug(f"Queuing speech: {text}")
            # Add to queue for processing
            self.tts_queue.put(text)
        except Exception as e:
            logger.error(f"Error queuing speech: {e}")
    
    def _tts_worker(self):
        """
        Worker thread that processes TTS requests from the queue.
        This ensures thread-safe, sequential TTS output.
        Runs continuously and gracefully handles GUI context.
        """
        try:
            while self.tts_active:
                try:
                    # Get text from queue with timeout to allow graceful shutdown
                    text = self.tts_queue.get(timeout=1)
                    if text is None:  # Sentinel value to stop worker
                        break
                    
                    # Use lock to ensure exclusive access to TTS engine
                    with self.tts_lock:
                        try:
                            logger.debug(f"Speaking: {text}")
                            self.tts_engine.say(text)
                            self.tts_engine.runAndWait()
                        except Exception as e:
                            logger.error(f"Error in TTS execution: {e}")
                    
                except queue.Empty:
                    # Timeout occurred, continue waiting
                    continue
                except Exception as e:
                    logger.error(f"Error in TTS worker: {e}")
        except Exception as e:
            logger.error(f"Fatal error in TTS worker thread: {e}")
    
    def _speak_thread(self, text):
        """Thread function for text-to-speech (legacy support)."""
        try:
            with self.tts_lock:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
        except Exception as e:
            logger.error(f"Error in TTS thread: {e}")
    
    def is_listening(self):
        """
        Check if microphone is available.
        
        Returns:
            bool: True if microphone is available, False otherwise
        """
        try:
            mic_kwargs = {}
            if MIC_INDEX is not None:
                try:
                    mic_kwargs['device_index'] = int(MIC_INDEX)
                except Exception:
                    pass
            with sr.Microphone(**mic_kwargs) as source:
                return True
        except Exception:
            return False
    
    @staticmethod
    def match_keyword(text, keywords):
        """
        Match text against a list of keywords.
        
        Args:
            text (str): Text to match
            keywords (list): List of keywords to match against
            
        Returns:
            bool: True if any keyword is found in text
        """
        text_lower = text.lower()
        return any(keyword.lower() in text_lower for keyword in keywords)
    
    def close(self):
        """Cleanup resources and stop TTS worker thread."""
        try:
            self.tts_active = False
            # Send sentinel value to stop worker thread
            self.tts_queue.put(None)
            # Wait for worker thread to finish
            if self.tts_worker_thread.is_alive():
                self.tts_worker_thread.join(timeout=2)
            
            if self.tts_engine:
                self.tts_engine.stop()
            logger.info("Speech Engine closed")
        except Exception as e:
            logger.error(f"Error closing Speech Engine: {e}")


# Global speech engine instance
_speech_engine = None


def get_speech_engine():
    """
    Get or create the global speech engine instance.
    
    Returns:
        SpeechEngine: Global speech engine instance
    """
    global _speech_engine
    if _speech_engine is None:
        _speech_engine = SpeechEngine()
    return _speech_engine


def speak(text):
    """Convenience function to speak text."""
    engine = get_speech_engine()
    engine.speak(text)


def listen():
    """Convenience function to listen for user input."""
    engine = get_speech_engine()
    return engine.listen()
