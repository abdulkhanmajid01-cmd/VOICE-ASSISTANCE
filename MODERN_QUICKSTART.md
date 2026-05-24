# 🚀 Quick Start Guide - Modern Jarvis Assistant

## Installation

Your Voice Assistant is already installed! Just run:

```bash
python main.py --gui
```

## First Use

1. **Start the Application**
   ```bash
   cd "c:\Users\lenovo\Desktop\voice assistance"
   python main.py --gui
   ```

2. **Wait for the Interface to Load**
   - You'll see a dark blue modern interface with "JARVIS" displayed
   - Green status dot = Ready and listening
   - Animated microphone shows on the left

3. **Say Your First Command**
   ```
   "Jarvis, open Google"
   
   or
   
   "Assistant, play Imagine Dragons"
   ```

## Command Examples

### 🎵 Music Commands
```
"Jarvis, play Blinding Lights"
"Assistant, play bad habit song"
"Play Levitating on YouTube"
```

### 🔍 Search Commands
```
"Search AI tools on Google"
"Search Python tutorials"
"Jarvis, look up machine learning"
```

### 🌐 Website Commands
```
"Open YouTube"
"Open Google"
"Visit GitHub"
"Go to Wikipedia"
```

### ⏰ Information Commands
```
"What's the time?"
"Tell me the date"
"What's the weather?"
"Show me the weather forecast"
```

### 📝 Notes & Reminders
```
"Save note important meeting at 3pm"
"Set reminder call mom tomorrow"
"Show my reminders"
```

### 🎮 Fun Commands
```
"Tell me a joke"
"Hello, how are you?"
"What's your name?"
```

## Wake Words

You can activate the assistant with any of these:
- **"Jarvis"**
- **"Assistant"**  
- **"Hey Jarvis"**
- **"Hey Assistant"**

After the wake word, give your command.

## GUI Layout

```
┌─────────────────────────────────────────┐
│  🟢 🎧 Listening in Background...        │  ← Status
├─────────────────────────────────────────┤
│                                           │
│   ┌────────────┐      ┌──────────────┐   │
│   │ 🎤 Animated│      │  📡 Voice    │   │
│   │  Microphone│      │  Wave Anim   │   │
│   └────────────┘      └──────────────┘   │
│                                           │
├─────────────────────────────────────────┤
│  Last Command: ✓ Opened Google          │
├─────────────────────────────────────────┤
│  [🎤 Listen Now]           [⏹ Exit]     │
└─────────────────────────────────────────┘
```

## Tips for Best Performance

1. **Speak Clearly**: Enunciate words clearly for better recognition
2. **Quiet Environment**: Use in relatively quiet areas
3. **Microphone Close**: Keep microphone at reasonable distance
4. **Natural Speech**: Speak like you would to Siri or Google Assistant
5. **One Command at a Time**: Wait for response before next command

## Troubleshooting

### "No speech detected"
- Make sure your microphone is working
- Speak louder and clearer
- Move closer to microphone
- Check if another app is using the microphone

### Commands not recognized
- Use the wake word first: "Jarvis, [command]"
- Speak more clearly
- Try simpler commands first
- Check internet connection for online features

### Background listening not working
- Ensure BACKGROUND_LISTENING is enabled in config
- Check microphone permissions
- Try restarting the application

## Advanced Features

### Manual Listening
Click **"🎤 Listen Now"** button to manually trigger listening mode.

### Check Command History
The "Last Command" area shows:
- ✓ = Command executed successfully  
- ✗ = Error occurred
- Command text and response

### Customization
Edit `config.py` to customize:
- Wake words
- UI colors
- Microphone sensitivity
- Voice speed/volume
- Timeouts

## Keyboard Shortcuts
- **Click Exit Button** or **Alt+F4** = Close application
- **Click Listen Now** = Manual listening

## Getting Help

If something doesn't work:
1. Check the terminal output for error messages
2. Verify microphone is connected and working
3. Make sure you said the wake word first
4. Try a simpler command
5. Restart the application

---

**Happy commanding! 🚀**

For detailed features, see JARVIS_FEATURES.md
