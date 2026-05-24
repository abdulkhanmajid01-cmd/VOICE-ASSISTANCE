"""
Configuration and Constants for Voice Assistant
This file contains all configuration settings and constants used throughout the application
"""

import os
from pathlib import Path

# ==================== APPLICATION SETTINGS ====================
APP_NAME = "Voice Assistant"
APP_VERSION = "2.0.0"
DEVELOPER = "abdul majid khan"
RELEASE_DATE = "2026"

# ==================== PATHS ====================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
NOTES_DIR = DATA_DIR / "notes"
REMINDERS_DIR = DATA_DIR / "reminders"
LOGS_DIR = DATA_DIR / "logs"

# Create directories if they don't exist
for directory in [DATA_DIR, NOTES_DIR, REMINDERS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# ==================== SPEECH RECOGNITION SETTINGS ====================
LANGUAGE = "en-US"
MIC_INDEX = None  # Use default microphone (set to specific index if needed)
SPEECH_TIMEOUT = 5  # Timeout for speech recognition in seconds (reduced for faster recognition)
SPEECH_PHRASE_LIMIT = 10  # Maximum phrases to listen to
LISTEN_TIMEOUT = 2  # Timeout for listening (seconds to wait for speech to start - reduced for speed)
ENERGY_THRESHOLD = 800  # Microphone energy threshold (lower = more sensitive - lowered for better detection)
DYNAMIC_ENERGY_THRESHOLD = True  # Enable adaptive noise cancellation
AMBIENT_NOISE_DURATION = 0.5  # Seconds to adjust for ambient noise (reduced for faster startup)

# ==================== TEXT-TO-SPEECH SETTINGS ====================
TTS_RATE = 200  # Speech rate (100-200 recommended - increased for faster speech)
TTS_VOLUME = 1.0  # Volume level (0.0-1.0) - Maximum volume for clarity
TTS_VOICE_ID = 0  # 0 for male, 1 for female (depends on system)

# ==================== WAKE WORD SETTINGS ====================
WAKE_WORDS = ["jarvis", "assistant", "hey jarvis", "hey assistant"]  # Wake words to activate assistant
WAKE_WORD_ENABLED = True  # Enable wake word detection
WAKE_WORD_SENSITIVITY = 0.7  # Sensitivity for wake word detection (0.0-1.0)
BACKGROUND_LISTENING = True  # Enable continuous background listening

# ==================== WEATHER SETTINGS ====================
WEATHER_API_KEY = "YOUR_API_KEY_HERE"  # Get from openweathermap.org
DEFAULT_CITY = "London"
TEMPERATURE_UNIT = "C"  # C for Celsius, F for Fahrenheit

# ==================== EMAIL SETTINGS ====================
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use App Password for Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ==================== GUI SETTINGS ====================
GUI_THEME_COLOR = "#0D1117"  # Dark background
GUI_ACCENT_COLOR = "#58A6FF"  # Modern blue
GUI_SECONDARY_COLOR = "#1F6FEB"  # Secondary blue
GUI_FONT_SIZE = 10
GUI_WINDOW_WIDTH = 900
GUI_WINDOW_HEIGHT = 700
GUI_THEME = "modern_dark"  # Theme name

# ==================== COMMAND RECOGNITION ====================
# Sensitivity for command matching (0.0-1.0)
COMMAND_SENSITIVITY = 0.6

# Maximum number of retries for failed commands
MAX_RETRIES = 2

# ==================== LOGGING ====================
DEBUG_MODE = True  # Set to False for production
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# ==================== FEATURE FLAGS ====================
ENABLE_WAKE_WORD = True  # Enable wake word detection
ENABLE_CHATBOT = True  # Enable AI chatbot
ENABLE_GUI = True  # Enable Tkinter GUI
ENABLE_EMAIL = False  # Enable email sending (requires configuration)
ENABLE_REMINDERS = True  # Enable reminder system
ENABLE_MUSIC = True  # Enable music player
ENABLE_BACKGROUND_LISTENING = True  # Enable continuous background listening

# ==================== MUSIC PLAYER SETTINGS ====================
MUSIC_FOLDERS = [
    os.path.expanduser("~/Music"),
    os.path.expanduser("~/Downloads"),
]
SUPPORTED_FORMATS = [".mp3", ".wav", ".flac", ".ogg"]

# ==================== SHORTCUTS ====================
WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "stackoverflow": "https://www.stackoverflow.com",
    "wikipedia": "https://www.wikipedia.org",
    "twitter": "https://www.twitter.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "gmail": "https://mail.google.com",
    "whatsapp": "https://web.whatsapp.com",
}

APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "wordpad": "wordpad.exe",
    "file explorer": "explorer.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
}

# ==================== RESPONSES ====================
GREETING_RESPONSES = [
    "Hello! How can I assist you today?",
    "Hi there! What can I help you with?",
    "Greetings! What would you like me to do?",
    "Hey! What do you need help with?",
]

FAREWELL_RESPONSES = [
    "Goodbye! Have a great day!",
    "See you later! Take care!",
    "Bye! It was nice helping you!",
    "Until next time! Goodbye!",
]

CONFUSED_RESPONSES = [
    "I'm not sure what you mean. Could you please repeat that?",
    "Sorry, I didn't quite catch that. Can you say it again?",
    "I don't understand. Could you clarify?",
    "Hmm, I'm not sure about that. Can you rephrase?",
]

# ==================== ERROR MESSAGES ====================
ERROR_MESSAGES = {
    "mic_not_found": "Microphone not found. Please check your microphone connection.",
    "no_internet": "Internet connection is required for this feature.",
    "api_error": "Unable to connect to the service. Please try again later.",
    "file_not_found": "The file you requested was not found.",
    "invalid_email": "Invalid email address.",
    "speech_recognition_error": "Could not understand audio. Please speak clearly.",
}
