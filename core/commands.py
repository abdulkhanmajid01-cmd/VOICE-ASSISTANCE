"""
Commands Module
Handles command recognition and routing to appropriate features
"""

import logging
from config import DEBUG_MODE, MAX_RETRIES
from core.speech_engine import SpeechEngine

# Import feature modules
from features.time_date import get_current_time, get_current_date
from features.web_browsing import open_website_command, search_google_command, search_youtube_command
from features.wikipedia_search import search_wikipedia
from features.music import play_music, list_music_files
from features.system import (
    open_app, shutdown_pc, restart_pc, lock_screen,
    get_cpu_usage, get_memory_usage, get_disk_usage
)
from features.weather import get_weather, format_weather_message
from features.conversation import (
    get_greeting, get_farewell, get_confused_response, chat_with_api
)
from features.notes import save_note, read_note, list_notes, delete_note, search_notes
from features.reminders import (
    add_reminder, list_all_reminders, get_upcoming_reminders,
    delete_reminder, check_reminders
)
from features.email_service import send_email, validate_email

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


class CommandProcessor:
    """
    Process voice commands and route them to appropriate features
    """
    
    def __init__(self):
        """Initialize command processor."""
        self.speech_engine = SpeechEngine()
        self.command_history = []
        logger.info("CommandProcessor initialized")
    
    def process_command(self, command):
        """
        Process a voice command and execute appropriate action.
        
        Args:
            command (str): Voice command text
            
        Returns:
            tuple: (executed: bool, response: str)
        """
        try:
            command = command.lower().strip()
            logger.info(f"Processing command: {command}")
            self.command_history.append(command)
            
            # Check for command matches
            response = self._route_command(command)
            
            if response:
                self.speech_engine.speak(response)
                return True, response
            else:
                confused = get_confused_response()
                self.speech_engine.speak(confused)
                return False, confused
        
        except Exception as e:
            logger.error(f"Error processing command: {e}")
            error_msg = "Sorry, an error occurred while processing your command."
            self.speech_engine.speak(error_msg)
            return False, error_msg
    
    def _route_command(self, command):
        """
        Route command to appropriate handler.
        
        Args:
            command (str): Command text
            
        Returns:
            str: Response message
        """
        # ==================== GREETING/FAREWELL ====================
        if any(word in command for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
            return get_greeting()
        
        if any(word in command for word in ["goodbye", "bye", "see you", "exit", "quit"]):
            return get_farewell()
        
        # ==================== TIME AND DATE ====================
        if any(word in command for word in ["time", "current time", "what time"]):
            return get_current_time()
        
        if any(word in command for word in ["date", "current date", "today"]):
            return get_current_date()
        
        # ==================== WEB BROWSING ====================
        if "open" in command or "visit" in command or "go to" in command:
            success, msg = open_website_command(command)
            return msg if success else None
        
        if "search google" in command or "google" in command:
            success, msg = search_google_command(command)
            return msg if success else None
        
        if "search youtube" in command or "youtube" in command:
            success, msg = search_youtube_command(command)
            return msg if success else None
        
        # ==================== WIKIPEDIA ====================
        if "search wikipedia" in command or "wikipedia" in command or "look up" in command:
            query = command.replace("search wikipedia for", "").replace("wikipedia", "").strip()
            if query:
                success, result = search_wikipedia(query)
                return result if success else None
        
        # ==================== MUSIC ====================
        if "play music" in command or "play a song" in command:
            success, msg = play_music()
            return msg if success else None
        
        if "stop music" in command or "pause music" in command:
            return "Music stopped"
        
        if "list songs" in command or "show music" in command:
            songs = list_music_files()
            if songs:
                return f"Found {len(songs)} songs: " + ", ".join(songs[:5])
            return "No songs found"
        
        # ==================== APPLICATIONS ====================
        if "open" in command and "application" in command:
            app_name = command.replace("open", "").replace("application", "").strip()
            if app_name:
                success, msg = open_app(app_name)
                return msg if success else None
        
        # Specific applications
        for app in ["notepad", "calculator", "paint", "chrome", "firefox"]:
            if f"open {app}" in command or f"start {app}" in command:
                success, msg = open_app(app)
                return msg if success else None
        
        # ==================== SYSTEM OPERATIONS ====================
        if "shutdown" in command:
            return "Shutting down the computer"
        
        if "restart" in command:
            return "Restarting the computer"
        
        if "lock screen" in command or "lock" in command:
            success, msg = lock_screen()
            return msg if success else None
        
        if "cpu usage" in command or "system usage" in command:
            cpu = get_cpu_usage()
            memory = get_memory_usage()
            return f"CPU usage is {cpu}%, Memory usage is {memory}%"
        
        # ==================== WEATHER ====================
        if "weather" in command or "temperature" in command or "forecast" in command:
            success, data = get_weather()
            if success:
                return format_weather_message(data)
            return None
        
        # ==================== NOTES ====================
        if "save note" in command or "add note" in command:
            # Extract title and content
            title = "Quick Note"
            content = command.replace("save note", "").replace("add note", "").strip()
            if content:
                success, msg = save_note(title, content)
                return msg if success else None
        
        if "read note" in command or "show notes" in command:
            notes = list_notes()
            if notes:
                return f"You have {len(notes)} notes: " + ", ".join(notes[:5])
            return "You don't have any notes"
        
        # ==================== REMINDERS ====================
        if "set reminder" in command or "remind me" in command:
            # Extract reminder message
            reminder_text = command.replace("set reminder", "").replace("remind me", "").strip()
            if reminder_text:
                success, msg = add_reminder("Reminder", reminder_text, "5 minutes")
                return msg if success else None
        
        if "show reminders" in command or "list reminders" in command:
            reminders = list_all_reminders()
            if reminders:
                return f"You have {len(reminders)} reminders"
            return "You don't have any reminders"
        
        if "check reminders" in command or "upcoming reminders" in command:
            upcoming = get_upcoming_reminders()
            if upcoming:
                return f"You have {len(upcoming)} upcoming reminders"
            return "No upcoming reminders"
        
        # ==================== EMAIL ====================
        if "send email" in command:
            return "Email sending feature requires configuration. Please set your email credentials."
        
        # ==================== CONVERSATION ====================
        # If no specific command matched, try to chat
        return chat_with_api(command)
    
    def get_command_history(self):
        """Get command history."""
        return self.command_history
    
    def clear_command_history(self):
        """Clear command history."""
        self.command_history = []
        logger.info("Command history cleared")
    
    def handle_continuous_listening(self):
        """
        Handle continuous listening for voice commands.
        This runs in a loop until interrupted.
        """
        try:
            logger.info("Starting continuous listening mode")
            print("Voice Assistant is listening... (Say 'exit' or 'bye' to quit)\n")
            
            while True:
                try:
                    # Listen for command
                    command = self.speech_engine.listen()
                    
                    if not command:
                        continue
                    
                    # Check for exit commands
                    if any(word in command for word in ["exit", "quit", "bye", "goodbye"]):
                        self.speech_engine.speak(get_farewell())
                        logger.info("Exiting continuous listening mode")
                        break
                    
                    # Process command
                    executed, response = self.process_command(command)
                    print(f"You: {command}")
                    print(f"Assistant: {response}\n")
                
                except KeyboardInterrupt:
                    logger.info("Interrupted by user")
                    self.speech_engine.speak("Goodbye!")
                    break
                except Exception as e:
                    logger.error(f"Error in continuous listening: {e}")
                    continue
        
        except Exception as e:
            logger.error(f"Fatal error in continuous listening: {e}")
    
    def handle_single_command(self):
        """Handle listening and processing a single command."""
        try:
            logger.info("Listening for single command")
            command = self.speech_engine.listen()
            
            if command:
                executed, response = self.process_command(command)
                return executed, response, command
            else:
                return False, "No command recognized", ""
        
        except Exception as e:
            logger.error(f"Error handling single command: {e}")
            return False, "An error occurred", ""


# Global command processor instance
_command_processor = None


def get_command_processor():
    """Get or create the global command processor instance."""
    global _command_processor
    if _command_processor is None:
        _command_processor = CommandProcessor()
    return _command_processor
