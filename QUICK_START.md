# Quick Start Guide - Voice Assistant

Get up and running in 5 minutes!

## 1️⃣ Install Python
Download from https://www.python.org/downloads/ (3.8 or higher)
- ✓ Check "Add Python to PATH"

## 2️⃣ Open Terminal/Command Prompt
```bash
# Navigate to project folder
cd C:\Users\YourName\Desktop\voice\ assistance
# OR
cd ~/Desktop/voice-assistance
```

## 3️⃣ Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
✓ Your prompt should now show `(venv)`

## 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
This takes 2-3 minutes. Wait for completion.

## 5️⃣ Run the Application!

### Option A: Interactive Mode (Type Commands)
```bash
python main.py
```
Then type: "What's the time?"

### Option B: GUI Mode (Visual Interface)
```bash
python main.py --gui
```

### Option C: Voice Mode (Speak Commands)
```bash
python main.py --voice
```

---

## 🎤 Try These Commands

Type or say these in interactive mode:
- "What's the time?"
- "Tell me the date"
- "Open Google"
- "Tell me a joke"
- "Search YouTube for Python"
- "Save note hello world"
- "Show notes"
- "exit"

---

## ⚙️ Optional: Configure Email (Gmail)

1. Go to https://myaccount.google.com/apppasswords
2. Generate password
3. Edit `config.py`:
```python
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-generated-password"
ENABLE_EMAIL = True
```

---

## 🆘 Common Issues

### "Microphone not found"
- Plug in microphone
- Restart terminal
- Try: `python main.py --single`

### "ModuleNotFoundError"
- Make sure virtual environment is activated (venv in prompt)
- Run: `pip install -r requirements.txt` again

### "No command recognized"
- Speak clearly and loudly
- Increase timeout: Edit config.py, set `SPEECH_TIMEOUT = 15`

---

## 📚 Next: Read Full Docs
- `README.md` - Full features and capabilities
- `INSTALLATION.md` - Detailed installation guide
- `config.py` - All configuration options

---

## 🎯 Common Modes

```bash
# Interactive (type commands)
python main.py

# GUI (graphical interface)
python main.py --gui

# Voice (speak commands)
python main.py --voice

# Single command
python main.py --single

# Demo
python main.py --demo

# Help
python main.py --help-commands
```

---

**That's it! You're ready to use Voice Assistant! 🚀**

For issues, see INSTALLATION.md troubleshooting section.
