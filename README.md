# Voice Assistant - Professional Python Application

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

A sophisticated, beginner-friendly Python-based voice assistant similar to Siri or Alexa. This project features speech recognition, text-to-speech, web automation, note-taking, reminders, and much more.

## 🌟 Key Features

### Core Features
- ✅ **Speech Recognition** - Understands voice commands using Google Speech API
- ✅ **Text-to-Speech** - Responds with natural-sounding voice
- ✅ **Web Browsing** - Opens websites and performs searches (Google, YouTube)
- ✅ **Information Lookup** - Wikipedia search and weather updates
- ✅ **Time & Date** - Current time, date, and scheduling
- ✅ **Music Player** - Play, stop, and manage music files
- ✅ **Note Taking** - Save, read, search, and manage notes
- ✅ **Reminders & Alarms** - Set and manage reminders
- ✅ **System Control** - Launch applications, check system stats
- ✅ **Natural Conversation** - Chat with built-in AI responses

### Advanced Features
- 🎨 **Graphical User Interface (GUI)** - Tkinter-based modern interface
- 🤖 **AI Chatbot** - Basic conversation responses (extensible with APIs)
- 📧 **Email Sending** - Send emails and reminders
- 🎯 **Wake Word Detection** - Customizable activation word
- 📊 **System Monitoring** - CPU, memory, disk usage
- 🔐 **Security Features** - Screen lock, shutdown control
- 📝 **Advanced Notes** - Search, export, organize notes
- ⏰ **Alarm System** - Set alarms with custom messages
- 📋 **Command History** - Track user commands
- 🌐 **Internet Integration** - Weather API, web searches

## 📁 Project Structure

```
voice-assistance/
├── main.py                      # Entry point with multiple modes
├── config.py                    # Configuration and constants
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── INSTALLATION.md              # Installation guide
│
├── core/                        # Core modules
│   ├── __init__.py
│   ├── speech_engine.py        # Speech recognition & TTS
│   ├── commands.py             # Command processing
│   └── utils.py                # Utility functions
│
├── features/                    # Feature modules
│   ├── __init__.py
│   ├── time_date.py            # Time & date features
│   ├── web_browsing.py         # Web search & navigation
│   ├── wikipedia_search.py     # Wikipedia integration
│   ├── music.py                # Music player
│   ├── system.py               # System operations
│   ├── weather.py              # Weather information
│   ├── conversation.py         # Chat responses
│   ├── notes.py                # Note management
│   ├── email_service.py        # Email functionality
│   └── reminders.py            # Reminders & alarms
│
├── gui/                         # GUI components
│   ├── __init__.py
│   └── assistant_gui.py        # Tkinter interface
│
└── data/                        # Runtime data
    ├── notes/                  # Saved notes
    ├── reminders/              # Reminder files
    └── logs/                   # Application logs
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Microphone and speakers
- 500 MB disk space
- Internet connection (for web features)

### Installation

#### Step 1: Clone or Download Project
```bash
# Navigate to project directory
cd voice-assistance
```

#### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Verify Installation
```bash
python main.py --version
```

## 💻 Running the Application

### Mode 1: Interactive Mode (Default)
Type commands instead of speaking:
```bash
python main.py
# or
python main.py --mode interactive
```

**Usage:**
- Type your command and press Enter
- Example: "What's the time?"
- Type "help" for available commands
- Type "exit" to quit

### Mode 2: Voice Mode (Continuous Listening)
Listen for voice commands continuously:
```bash
python main.py --voice
# or
python main.py --mode voice
# or
python main.py --continuous
```

**Usage:**
- Assistant listens for voice commands
- Speak your command clearly
- Say "exit" or "goodbye" to quit

### Mode 3: Single Voice Command
Listen for one voice command:
```bash
python main.py --single
```

### Mode 4: GUI Mode (Graphical Interface)
Run with graphical interface:
```bash
python main.py --gui
# or
python main.py --mode gui
```

**Features:**
- Modern tabbed interface
- Visual display of information
- Easy-to-use buttons
- Real-time status updates

### Mode 5: Demo Mode
See the assistant in action:
```bash
python main.py --demo
# or
python main.py --mode demo
```

### Show Help Commands
```bash
python main.py --help-commands
```

## 🎤 Voice Commands

### Time & Date Commands
```
"What's the time?"
"Tell me the date"
"What day is it?"
"Current time"
```

### Web Browsing Commands
```
"Open Google"
"Go to YouTube"
"Visit Wikipedia"
"Search Google for [query]"
"Search YouTube for [query]"
```

### Information Commands
```
"What's the weather?"
"Search Wikipedia for [topic]"
"Wikipedia search [topic]"
```

### Music Commands
```
"Play music"
"Stop music"
"List my music"
```

### Application Commands
```
"Open Notepad"
"Open Calculator"
"Open Chrome"
"Open Firefox"
"Open Paint"
```

### System Commands
```
"CPU usage"
"System usage"
"Lock screen"
"Shutdown"
"Restart"
```

### Notes Commands
```
"Save note [content]"
"Show notes"
"Read my notes"
```

### Reminder Commands
```
"Set reminder [text]"
"Show reminders"
"Check upcoming reminders"
```

### Conversation Commands
```
"Hello"
"How are you?"
"What's your name?"
"Tell me a joke"
"Good morning"
"Thank you"
```

## ⚙️ Configuration

Edit `config.py` to customize:

### Speech Settings
```python
LANGUAGE = "en-US"              # Change language
TTS_RATE = 150                  # Speech speed
TTS_VOLUME = 0.9                # Volume level
SPEECH_TIMEOUT = 10             # Listening timeout
```

### Wake Word
```python
WAKE_WORD = "hey assistant"
ENABLE_WAKE_WORD = False        # Set to True to enable
```

### Email Configuration
```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
ENABLE_EMAIL = True
```

### Weather Configuration
```python
WEATHER_API_KEY = "YOUR_API_KEY"
DEFAULT_CITY = "London"
```

### Feature Flags
```python
ENABLE_GUI = True
ENABLE_CHATBOT = True
ENABLE_REMINDERS = True
```

## 🔧 Advanced Setup

### Gmail Email Configuration
1. Enable 2-Step Verification on Gmail
2. Generate App Password: https://myaccount.google.com/apppasswords
3. Copy the app password to config.py
4. Set `ENABLE_EMAIL = True`

### Weather API Setup
1. Get free API key from: https://openweathermap.org/
2. Set API key in config.py
3. Update DEFAULT_CITY

### Adding Custom Applications
Edit the `APPLICATIONS` dictionary in `config.py`:
```python
APPLICATIONS = {
    "your_app": "C:/Path/To/Application.exe",
}
```

### Adding Custom Websites
Edit the `WEBSITES` dictionary in `config.py`:
```python
WEBSITES = {
    "my_site": "https://mywebsite.com",
}
```

## 📊 Project Statistics

- **Total Lines of Code:** ~4,500+
- **Modules:** 15+
- **Features:** 50+
- **Commands:** 100+
- **Dependencies:** 8 core packages

## 🎓 Educational Value

This project is suitable for:
- ✓ University final year projects
- ✓ Portfolio development
- ✓ Python learning
- ✓ AI/ML workshops
- ✓ Capstone projects
- ✓ Hackathons

**Skills Demonstrated:**
- Object-Oriented Programming
- API Integration
- GUI Development
- Speech Processing
- File Management
- Error Handling
- Logging
- Documentation

## 🐛 Troubleshooting

### Microphone Not Found
```
Error: Microphone not found. Please check your microphone connection.

Solution:
1. Check microphone is connected
2. In config.py, set: MIC_INDEX = 1 (try different indexes)
3. Test with: python -c "import speech_recognition; print(speech_recognition.Microphone.list_microphone_indexes())"
```

### Speech Recognition Not Working
```
Error: Could not understand audio.

Solution:
1. Speak more clearly
2. Reduce background noise
3. Increase microphone gain
4. Check internet connection (Google Speech API requires internet)
5. Increase SPEECH_TIMEOUT in config.py
```

### Audio Playback Issues
```
Solution:
1. Check speakers are connected
2. Test volume: python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('test'); engine.runAndWait()"
3. Try different TTS_VOICE_ID in config.py
```

### Import Errors
```
Solution:
1. Ensure virtual environment is activated
2. Reinstall dependencies: pip install -r requirements.txt
3. Check Python version: python --version (should be 3.8+)
```

## 📚 Documentation

- **Full Installation Guide:** See [INSTALLATION.md](INSTALLATION.md)
- **Code Comments:** Extensive inline documentation
- **Docstrings:** Every function has usage documentation

## 🔐 Security Considerations

- Sensitive data (email, passwords) stored in config.py
- Consider using environment variables for production
- Email passwords should use app-specific passwords
- Never share config.py publicly

## 📈 Future Enhancements

- [ ] Machine learning for command recognition
- [ ] Integration with Smart Home APIs
- [ ] Multi-language support
- [ ] Voice cloning
- [ ] Database for notes/reminders
- [ ] Cloud synchronization
- [ ] Mobile app companion
- [ ] Custom hotword detection
- [ ] Advanced NLP
- [ ] Real-time translation

## 🤝 Contributing

Feel free to fork and improve this project!

## 📄 License

MIT License - Feel free to use in personal and commercial projects

## 👨‍💼 Author

**Abdul majid khan**
- University: Your University
- Year: 2026

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the code comments
3. Check config.py settings
4. See INSTALLATION.md for detailed setup

## 🎉 Acknowledgments

- Google Speech Recognition API
- pyttsx3 for text-to-speech
- Wikipedia API for information
- Open-Meteo for weather data
- Python community for excellent libraries

---

**Developed as a Professional University Project**

*This project demonstrates professional Python development practices suitable for production environments and advanced academic submissions.*
