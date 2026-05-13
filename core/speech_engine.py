"""
Speech Engine Module
Handles speech recognition and text-to-speech functionality
"""

import speech_recognition as sr
import pyttsx3
import logging
import threading
from config import (
    LANGUAGE, TTS_RATE, TTS_VOLUME, TTS_VOICE_ID,
    SPEECH_TIMEOUT, LISTEN_TIMEOUT, ERROR_MESSAGES, DEBUG_MODE
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
            # Initialize speech recognizer
            self.recognizer = sr.Recognizer()
            self.recognizer.energy_threshold = 4000  # Adjust sensitivity
            
            # Initialize text-to-speech engine
            self.tts_engine = pyttsx3.init()
            self._configure_tts()
            
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
        Listen to user voice input.
        
        Args:
            timeout (int): Maximum time to listen in seconds
            
        Returns:
            str: Recognized text from speech, or empty string if failed
        """
        try:
            with sr.Microphone() as source:
                logger.debug("Listening for audio input...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=LISTEN_TIMEOUT, phrase_time_limit=timeout)
            
            # Recognize speech using Google Speech Recognition
            try:
                text = self.recognizer.recognize_google(audio, language=LANGUAGE)
                logger.info(f"Recognized: {text}")
                return text.lower()
            except sr.UnknownValueError:
                logger.warning("Could not understand audio")
                return ""
            except sr.RequestError as e:
                logger.error(f"Google Speech Recognition error: {e}")
                return ""
        
        except (OSError, Exception) as e:
            logger.error(f"Microphone error: {e}")
            return ""
        except Exception as e:
            logger.error(f"Unexpected error during listening: {e}")
            return ""
    
    def speak(self, text):
        """
        Convert text to speech and play it.
        
        Args:
            text (str): Text to be spoken
        """
        try:
            logger.debug(f"Speaking: {text}")
            # Run TTS in a separate thread to avoid blocking the GUI
            tts_thread = threading.Thread(target=self._speak_thread, args=(text,))
            tts_thread.daemon = True
            tts_thread.start()
        except Exception as e:
            logger.error(f"Error in text-to-speech: {e}")
    
    def _speak_thread(self, text):
        """Thread function for text-to-speech."""
        try:
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
            with sr.Microphone() as source:
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
        """Cleanup resources."""
        try:
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
