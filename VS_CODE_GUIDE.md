# Running Voice Assistant in VS Code - Complete Guide

## Setup VS Code for Voice Assistant

### Step 1: Open Project in VS Code

1. Open VS Code
2. File → Open Folder
3. Navigate to: `C:\Users\lenovo\Desktop\voice assistance`
4. Select folder and click "Select Folder"

### Step 2: Install Python Extension

1. Click Extensions icon (left sidebar) or Ctrl+Shift+X
2. Search: "Python"
3. Install "Python" by Microsoft (top result)
4. Also install "Pylance" for better intellisense

### Step 3: Select Python Interpreter

1. Press Ctrl+Shift+P
2. Type: "Python: Select Interpreter"
3. Choose: "Create Virtual Environment"
4. Choose: "venv"
5. Select: "Python 3.x.x"
6. Wait for virtual environment to be created

### Step 4: Terminal Setup

1. Press Ctrl+` to open terminal (or View → Terminal)
2. If not activated, manually activate:
   ```bash
   # Windows
   .venv\Scripts\activate
   # or
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

### Step 5: Install Dependencies

In VS Code terminal:
```bash
pip install -r requirements.txt
```

This may take 2-3 minutes. Wait for completion.

### Step 6: Verify Installation

```bash
# Check Python version
python --version

# Check if modules installed
pip list
```

## Running the Application in VS Code

### Method 1: Using Terminal (Recommended for Beginners)

1. Open Terminal: Ctrl+`
2. Make sure terminal shows: (venv) C:\path\to\project>
3. Run command:
   ```bash
   python main.py
   ```
4. Follow the prompts
5. Type commands like: "What's the time?"

### Method 2: Using Run and Debug

1. Open main.py file
2. Press Ctrl+Shift+D (or Run icon on left)
3. Click "Create a launch.json file"
4. Select "Python" environment
5. Click green play button ▶

Or setup custom configurations:

1. Click Run and Debug icon (or Ctrl+Shift+D)
2. Create launch.json (if not exists)
3. Click "create a launch.json file" → Python
4. Replace with:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Interactive Mode",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "GUI Mode",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "args": ["--gui"],
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Voice Mode",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "args": ["--voice"],
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Demo Mode",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "args": ["--demo"],
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

Now you can select which mode to run:
1. Click dropdown at top of Run panel
2. Select mode: "Interactive Mode", "GUI Mode", etc.
3. Click green play button ▶

### Method 3: Run Python File Directly

1. Right-click on main.py
2. Select "Run Python File in Terminal"
3. This runs in interactive mode

### Method 4: Using Code Runner Extension (Optional)

1. Install "Code Runner" extension
2. Right-click in main.py
3. Select "Run Code"
4. Or press Ctrl+Alt+N

## VS Code Tips & Tricks

### Open Terminal with Virtual Environment

VS Code automatically activates venv if configured correctly.

If not, in terminal type:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### View Output

All output shows in the "Terminal" panel at bottom.

### Debug with Breakpoints

1. Click left of line number (red dot appears)
2. Press F5 or click play button
3. Execution stops at breakpoint
4. View variables in Debug panel

### IntelliSense/Auto-Complete

Type variable name and press Ctrl+Space for suggestions:
```python
from core.speech_engine import get_speech_engine

engine = get_speech_engine()
engine.  # <- Ctrl+Space shows available methods
```

### Go to Definition

Hold Ctrl and click on function name, or:
- Right-click → "Go to Definition"
- Press Ctrl+G to go to line

### Find and Replace

- Find: Ctrl+F
- Replace: Ctrl+H
- Find in all files: Ctrl+Shift+F

### Format Code

Select code or press Ctrl+A for all:
```bash
Ctrl+Shift+P → Python: Format Document
```

Or install Black formatter:
```bash
pip install black
# Then Ctrl+Shift+P → Format Document
```

### Run Tests (Optional)

If you create test files:
```bash
pip install pytest
pytest
# or in VS Code: Python: Run Tests
```

## File Explorer Navigation

Left sidebar shows project structure:
- main.py (entry point)
- config.py (settings)
- core/ (speech, commands)
- features/ (all features)
- gui/ (graphical interface)
- data/ (runtime files)

Click on any file to open in editor.

## Common Workflows

### Workflow 1: Testing Commands

1. Open Terminal (Ctrl+`)
2. Activate venv
3. Run: `python main.py`
4. Type commands
5. See output in terminal

### Workflow 2: Editing Code

1. Open file in editor
2. Make changes
3. Save: Ctrl+S
4. Run terminal command to test
5. Check output

### Workflow 3: Debugging

1. Set breakpoint (click line number)
2. Press F5 or click Run
3. Execution pauses at breakpoint
4. View variables in Debug panel
5. Press F10 to step, F5 to continue

### Workflow 4: Checking Documentation

1. Right-click function name
2. Select "Go to Definition"
3. Read docstring and comments
4. Use Peek Definition (Alt+F12) to preview

## Troubleshooting in VS Code

### Python Not Found

1. Ctrl+Shift+P → "Python: Select Interpreter"
2. If showing: ".venv: Recommended"
3. Click it
4. Verify terminal now shows: (venv)

### Terminal Won't Activate

1. Close terminal (X button)
2. Open new terminal: Ctrl+`
3. Should auto-activate with .venv

### Can't Find requirements.txt

1. Make sure you opened the correct folder
2. Folder should contain main.py and requirements.txt
3. Not the parent folder

### Pylance Errors

1. These are usually just warnings
2. Can ignore them
3. App will still run fine
4. Or install dependencies it suggests

### GUI Doesn't Open

1. Tkinter may need separate installation
2. Windows: Usually included, try: `python main.py --gui`
3. macOS: `brew install python-tk`
4. Linux: `sudo apt-get install python3-tk`

## Essential Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Terminal | Ctrl+` |
| Open File | Ctrl+O |
| Save | Ctrl+S |
| Find | Ctrl+F |
| Replace | Ctrl+H |
| Run Debug | F5 |
| Stop Debug | Shift+F5 |
| Step Over | F10 |
| Step Into | F11 |
| Run Python File | Ctrl+Alt+N (Code Runner) |
| Command Palette | Ctrl+Shift+P |
| Go to Definition | Ctrl+Click or F12 |
| Select Interpreter | Ctrl+Shift+P → Python: Select Interpreter |

## Recommended VS Code Settings

Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.python",
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "terminal.integrated.defaultProfile.windows": "Command Prompt",
    "python.analysis.typeCheckingMode": "basic"
}
```

## Summary

**Quickest Way to Run:**

1. Open project in VS Code
2. Press Ctrl+` (open terminal)
3. Terminal should show: (venv) C:\path>
4. Type: `python main.py`
5. Use the app!

**First Time Setup (Do Once):**

1. Ctrl+Shift+P → Python: Select Interpreter → Create Virtual Environment
2. In terminal: `pip install -r requirements.txt`
3. Done! Now just use `python main.py`

**Debugging:**

1. Click line number to set breakpoint (red dot)
2. Press F5 to start debug
3. Use F10 to step through code
4. View variables in Debug panel

---

**You're all set! Start with: `python main.py` in VS Code terminal**
