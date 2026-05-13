# Installation Guide - Voice Assistant

Complete step-by-step guide for installing and running the Voice Assistant project.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Pre-Installation](#pre-installation)
3. [Installation Steps](#installation-steps)
4. [Post-Installation Setup](#post-installation-setup)
5. [Running the Application](#running-the-application)
6. [Troubleshooting](#troubleshooting)
7. [Uninstallation](#uninstallation)

---

## System Requirements

### Minimum Requirements
- **OS:** Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python:** 3.8 or higher
- **RAM:** 2 GB minimum
- **Disk Space:** 500 MB
- **Microphone:** Required for voice input
- **Speakers:** Required for audio output

### Recommended Requirements
- **OS:** Windows 11, macOS 12+, or Linux Ubuntu 22.04+
- **Python:** 3.10 or higher
- **RAM:** 4 GB
- **Disk Space:** 1 GB
- **Internet:** Broadband connection (for web features)
- **Microphone:** High-quality USB microphone
- **Speakers:** Decent quality speakers or headphones

### Check Your System
```bash
# Check Python version
python --version        # Should be 3.8 or higher

# Check pip
pip --version          # Should be installed with Python

# Check OS
# Windows
systeminfo | find "OS"

# macOS
system_profiler SPSoftwareDataType

# Linux
uname -a
```

---

## Pre-Installation

### Step 1: Install Python

#### Windows
1. Download from https://www.python.org/downloads/
2. Run installer
3. **IMPORTANT:** Check "Add Python to PATH"
4. Click "Install Now"
5. Verify: Open Command Prompt and run `python --version`

#### macOS
```bash
# Using Homebrew (recommended)
brew install python3

# Or download from python.org
# Then verify
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
```

### Step 2: Check pip
```bash
# Windows
pip --version

# macOS/Linux
pip3 --version
```

### Step 3: Install Audio Libraries

#### Windows
No action needed - audio libraries are platform-independent in Python

#### macOS
```bash
# Install PortAudio (required for PyAudio)
brew install portaudio
```

#### Linux (Ubuntu/Debian)
```bash
# Install audio development libraries
sudo apt-get install portaudio19-dev python3-pyaudio
```

---

## Installation Steps

### Step 1: Download Project
```bash
# Option 1: If you have the folder
cd C:\Users\YourName\Desktop\voice assistance
# or
cd ~/Desktop/voice\ assistance
# or
cd /home/username/voice-assistance

# Option 2: If cloning from GitHub
git clone https://github.com/your-repo/voice-assistant.git
cd voice-assistant
```

### Step 2: Create Virtual Environment

#### Windows
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Your prompt should now show (venv)
```

#### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should now show (venv)
```

### Step 3: Upgrade pip
```bash
# Windows, macOS, Linux
pip install --upgrade pip
```

### Step 4: Install Requirements

#### Option A: Standard Installation
```bash
pip install -r requirements.txt
```

#### Option B: Verbose Installation (Shows progress)
```bash
pip install -r requirements.txt -v
```

#### Option C: Install Individually
```bash
pip install speech-recognition==3.10.1
pip install pyttsx3==2.90
pip install pyaudio==0.2.13
pip install wikipedia==1.4.0
pip install requests==2.31.0
pip install psutil==5.9.6
```

### Step 5: Verify Installation
```bash
# Test imports
python -c "import speech_recognition; print('✓ speech_recognition installed')"
python -c "import pyttsx3; print('✓ pyttsx3 installed')"
python -c "import wikipedia; print('✓ wikipedia installed')"
python -c "import psutil; print('✓ psutil installed')"
```

---

## Post-Installation Setup

### Configuration Setup

#### 1. Email Setup (Optional)
To enable email sending:

**For Gmail:**
1. Go to https://myaccount.google.com
2. Enable 2-Step Verification
3. Go to https://myaccount.google.com/apppasswords
4. Generate App Password for "Mail" and "Windows Computer"
5. Copy the password
6. Edit `config.py`:
```python
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-generated-app-password"
ENABLE_EMAIL = True
```

#### 2. Weather Setup (Optional)
1. Visit https://openweathermap.org/api
2. Sign up for free account
3. Get API key from account
4. Edit `config.py`:
```python
WEATHER_API_KEY = "your-api-key-here"
DEFAULT_CITY = "Your City"
```

#### 3. Microphone Configuration (if needed)
1. Connect microphone to computer
2. Test microphone: `python -c "import speech_recognition; print(speech_recognition.Microphone.list_microphone_indexes())"`
3. Note the index number
4. Edit `config.py`:
```python
MIC_INDEX = 0  # Change 0 to your microphone index
```

#### 4. GUI Configuration (Optional)
Edit `config.py` for GUI customization:
```python
GUI_WINDOW_WIDTH = 800
GUI_WINDOW_HEIGHT = 600
GUI_THEME_COLOR = "#2C3E50"
GUI_ACCENT_COLOR = "#3498DB"
```

### Initial Test
```bash
# Make sure virtual environment is activated
# (venv) should show in your prompt

# Test the application
python main.py --help

# If this works, installation is successful!
```

---

## Running the Application

### Quick Start
```bash
# Activate virtual environment first
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Run in interactive mode (default)
python main.py
```

### Running in Different Modes

#### 1. Interactive Mode (Recommended for Testing)
```bash
python main.py
# or
python main.py --mode interactive
```
**What it does:** Type commands instead of speaking

#### 2. Voice Mode (Continuous Listening)
```bash
python main.py --voice
# or
python main.py --continuous
```
**What it does:** Assistant listens continuously for voice commands

#### 3. GUI Mode (Graphical Interface)
```bash
python main.py --gui
# or
python main.py --mode gui
```
**What it does:** Opens a nice graphical interface

#### 4. Demo Mode
```bash
python main.py --demo
# or
python main.py --mode demo
```
**What it does:** Shows what the assistant can do

#### 5. Single Voice Command
```bash
python main.py --single
```
**What it does:** Listen for one voice command and exit

#### 6. Show Help
```bash
python main.py --help-commands
```
**What it does:** Show all available voice commands

### Running from VS Code

#### Method 1: Using Terminal
1. Open Terminal in VS Code (Ctrl + `)
2. Activate virtual environment:
   ```bash
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```
3. Run the application:
   ```bash
   python main.py
   ```

#### Method 2: Using Run & Debug
1. Click on "Run" menu → "Start Debugging"
2. Select Python interpreter
3. This runs main.py automatically

#### Method 3: Using Python Extension
1. Right-click main.py
2. Select "Run Python File in Terminal"

#### Creating VS Code Launch Configuration
Create `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Voice Assistant - Interactive",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal"
        },
        {
            "name": "Voice Assistant - GUI",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "args": ["--gui"],
            "console": "integratedTerminal"
        },
        {
            "name": "Voice Assistant - Voice Mode",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "args": ["--voice"],
            "console": "integratedTerminal"
        }
    ]
}
```

---

## Troubleshooting

### Issue: "Python not found"
```
Error: 'python' is not recognized

Solution:
1. Check if Python is installed: python --version
2. Add Python to PATH (Windows):
   - Control Panel → System → Advanced System Settings
   - Environment Variables → Add C:\Python310\ to PATH
3. Restart Command Prompt/Terminal
4. Try: python --version
```

### Issue: "pip: command not found"
```
Error: pip is not installed or not in PATH

Solution:
1. Upgrade pip: python -m pip install --upgrade pip
2. Try using python -m pip instead of pip
3. Use: python -m pip install -r requirements.txt
```

### Issue: Virtual Environment Not Activating
```
Windows:
- Use full path: C:\path\to\venv\Scripts\activate
- In PowerShell: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
- Then: venv\Scripts\Activate.ps1

macOS/Linux:
- Use: source /path/to/venv/bin/activate
- Check: which python (should show venv path)
```

### Issue: "ModuleNotFoundError: No module named 'speech_recognition'"
```
Solution:
1. Activate virtual environment
2. Run: pip list (check if packages are installed)
3. Reinstall: pip install speech-recognition
4. If still fails: pip install --upgrade --force-reinstall speech-recognition
```

### Issue: Microphone Not Working
```
Solution:
1. Check microphone is connected: audio settings
2. Test Python access: python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_indexes())"
3. Update MIC_INDEX in config.py
4. Increase timeout: SPEECH_TIMEOUT = 15 in config.py
5. Test with: python main.py --single
```

### Issue: "Audio" or Sound Issues
```
Solution:
1. Check speaker volume
2. Test: python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('test'); engine.runAndWait()"
3. Try different voice: TTS_VOICE_ID = 1 in config.py
4. Slow down speech: TTS_RATE = 100 in config.py
```

### Issue: Cannot Import GUI Components
```
Error: ModuleNotFoundError: No module named 'tkinter'

Solution:
Windows: Tkinter comes with Python (ensure installed during Python setup)
macOS: brew install python-tk
Ubuntu: sudo apt-get install python3-tk
```

### Issue: "No module named 'config'"
```
Solution:
1. Ensure you're running from project root directory
2. Check config.py exists in project folder
3. Run: python main.py (not from other directories)
4. Try: python -m main
```

### Issue: Internet Required Errors
```
Solution:
1. Check internet connection: ping google.com
2. Disable firewall temporarily (if safe)
3. Check proxy settings
4. Use VPN if in restricted network
5. Some features require internet (weather, Wikipedia, web search)
```

---

## Uninstallation

### Complete Removal

#### Windows
```bash
# Deactivate virtual environment
deactivate

# Delete project folder
rmdir /s "C:\Users\YourName\Desktop\voice assistance"

# Or use File Explorer to delete
```

#### macOS/Linux
```bash
# Deactivate virtual environment
deactivate

# Delete project folder
rm -rf ~/Desktop/voice-assistance
```

### Just Deactivate Virtual Environment
```bash
# Keeps project, just disables virtual environment
deactivate
```

### Clean Cache (Optional)
```bash
# Remove Python cache files
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

---

## Next Steps

1. **Customize Configuration**
   - Edit config.py for your preferences
   - Add your email (Gmail)
   - Set weather location

2. **Test Features**
   - Run: `python main.py --demo`
   - Try different commands
   - Test microphone

3. **Explore the Code**
   - Read the documentation in code
   - Understand the structure
   - Modify for your needs

4. **Add Custom Features**
   - Create new feature modules
   - Add to commands.py
   - Test thoroughly

5. **Deployment**
   - Package for distribution
   - Create executable (.exe on Windows)
   - Share with others

---

## Support & Help

- **Python Documentation:** https://docs.python.org/3/
- **Project README:** See README.md
- **Code Comments:** Extensive documentation in source code
- **Error Messages:** Read carefully, they often indicate the solution

---

**Installation Complete!** 🎉

You're ready to use the Voice Assistant. Start with `python main.py` and follow the prompts.

Enjoy your voice-powered Python assistant!
