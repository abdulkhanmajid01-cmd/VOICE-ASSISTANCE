"""
GUI Module - Tkinter Interface
Provides a graphical user interface for the Voice Assistant
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import logging
import threading
from datetime import datetime
from config import (
    APP_NAME, APP_VERSION, GUI_THEME_COLOR, GUI_ACCENT_COLOR,
    GUI_FONT_SIZE, GUI_WINDOW_WIDTH, GUI_WINDOW_HEIGHT, DEBUG_MODE
)
from core.speech_engine import get_speech_engine, listen, speak
from core.commands import get_command_processor
from features.time_date import get_current_time, get_current_date
from features.weather import get_weather, format_weather_message, is_weather_available
from features.conversation import get_greeting, get_random_joke
from features.notes import list_notes, read_note, save_note
from features.reminders import list_all_reminders, get_upcoming_reminders

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


class VoiceAssistantGUI:
    """
    Graphical User Interface for Voice Assistant using Tkinter
    """
    
    def __init__(self, root):
        """Initialize the GUI."""
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.speech_engine = get_speech_engine()
        self.command_processor = get_command_processor()
        
        logger.info("GUI initialized")
    
    def setup_window(self):
        """Configure the main window."""
        self.root.title(f"{APP_NAME} v{APP_VERSION}")
        self.root.geometry(f"{GUI_WINDOW_WIDTH}x{GUI_WINDOW_HEIGHT}")
        self.root.configure(bg=GUI_THEME_COLOR)
        
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create GUI widgets."""
        # Header
        header_frame = tk.Frame(self.root, bg=GUI_ACCENT_COLOR, height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            header_frame,
            text=APP_NAME,
            font=("Arial", 18, "bold"),
            bg=GUI_ACCENT_COLOR,
            fg="white"
        )
        title_label.pack(pady=10)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg=GUI_THEME_COLOR)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Notebook (tabs)
        notebook = ttk.Notebook(content_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_home_tab(notebook)
        self.create_info_tab(notebook)
        self.create_notes_tab(notebook)
        self.create_reminders_tab(notebook)
        self.create_settings_tab(notebook)
        
        # Control panel
        control_frame = tk.Frame(self.root, bg=GUI_THEME_COLOR)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Buttons
        listen_btn = tk.Button(
            control_frame,
            text="🎤 Listen",
            command=self.listen_command,
            bg=GUI_ACCENT_COLOR,
            fg="white",
            font=("Arial", 10, "bold"),
            width=15
        )
        listen_btn.pack(side=tk.LEFT, padx=5)
        
        speak_btn = tk.Button(
            control_frame,
            text="🔊 Speak",
            command=self.speak_demo,
            bg=GUI_ACCENT_COLOR,
            fg="white",
            font=("Arial", 10, "bold"),
            width=15
        )
        speak_btn.pack(side=tk.LEFT, padx=5)
        
        exit_btn = tk.Button(
            control_frame,
            text="❌ Exit",
            command=self.root.quit,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15
        )
        exit_btn.pack(side=tk.RIGHT, padx=5)
    
    def create_home_tab(self, notebook):
        """Create home tab."""
        home_frame = tk.Frame(notebook, bg=GUI_THEME_COLOR)
        notebook.add(home_frame, text="Home")
        
        # Greeting
        greeting_label = tk.Label(
            home_frame,
            text=get_greeting(),
            font=("Arial", 12),
            bg=GUI_THEME_COLOR,
            fg="white"
        )
        greeting_label.pack(pady=20)
        
        # Status
        status_frame = tk.LabelFrame(
            home_frame,
            text="Quick Status",
            bg=GUI_THEME_COLOR,
            fg="white",
            font=("Arial", 10, "bold")
        )
        status_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        status_text = scrolledtext.ScrolledText(
            status_frame,
            height=10,
            width=50,
            bg="#34495E",
            fg="white",
            font=("Courier", 9)
        )
        status_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Get system info
        status_info = f"""
Time: {datetime.now().strftime('%H:%M:%S')}
Date: {datetime.now().strftime('%A, %B %d, %Y')}

System Status: Ready
Microphone: Available
Voice Recognition: Active

Quick Access:
- Click 'Listen' to give voice commands
- Click 'Speak' to hear a demo
- Use tabs for different features
        """
        status_text.insert(tk.END, status_info)
        status_text.config(state=tk.DISABLED)
    
    def create_info_tab(self, notebook):
        """Create information tab."""
        info_frame = tk.Frame(notebook, bg=GUI_THEME_COLOR)
        notebook.add(info_frame, text="Info")
        
        # Time and Date
        time_date_frame = tk.LabelFrame(
            info_frame,
            text="Current Time & Date",
            bg=GUI_THEME_COLOR,
            fg="white"
        )
        time_date_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            time_date_frame,
            text=get_current_time(),
            font=("Arial", 12),
            bg=GUI_THEME_COLOR,
            fg="white"
        ).pack(pady=5)
        
        tk.Label(
            time_date_frame,
            text=get_current_date(),
            font=("Arial", 12),
            bg=GUI_THEME_COLOR,
            fg="white"
        ).pack(pady=5)
        
        # Weather
        if is_weather_available():
            weather_frame = tk.LabelFrame(
                info_frame,
                text="Weather",
                bg=GUI_THEME_COLOR,
                fg="white"
            )
            weather_frame.pack(fill=tk.X, padx=10, pady=5)
            
            weather_btn = tk.Button(
                weather_frame,
                text="Get Weather",
                command=self.show_weather,
                bg=GUI_ACCENT_COLOR,
                fg="white"
            )
            weather_btn.pack(pady=5)
        
        # Joke
        joke_frame = tk.LabelFrame(
            info_frame,
            text="Fun",
            bg=GUI_THEME_COLOR,
            fg="white"
        )
        joke_frame.pack(fill=tk.X, padx=10, pady=5)
        
        joke_btn = tk.Button(
            joke_frame,
            text="Tell me a Joke",
            command=self.show_joke,
            bg=GUI_ACCENT_COLOR,
            fg="white"
        )
        joke_btn.pack(pady=5)
    
    def create_notes_tab(self, notebook):
        """Create notes tab."""
        notes_frame = tk.Frame(notebook, bg=GUI_THEME_COLOR)
        notebook.add(notes_frame, text="Notes")
        
        # Note list
        list_frame = tk.LabelFrame(
            notes_frame,
            text="My Notes",
            bg=GUI_THEME_COLOR,
            fg="white"
        )
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        notes_listbox = tk.Listbox(
            list_frame,
            bg="#34495E",
            fg="white"
        )
        notes_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Populate notes
        for note in list_notes():
            notes_listbox.insert(tk.END, note)
        
        # Buttons
        button_frame = tk.Frame(notes_frame, bg=GUI_THEME_COLOR)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(
            button_frame,
            text="New Note",
            bg=GUI_ACCENT_COLOR,
            fg="white"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Delete Note",
            bg="#E74C3C",
            fg="white"
        ).pack(side=tk.LEFT, padx=5)
    
    def create_reminders_tab(self, notebook):
        """Create reminders tab."""
        reminders_frame = tk.Frame(notebook, bg=GUI_THEME_COLOR)
        notebook.add(reminders_frame, text="Reminders")
        
        # Reminders list
        list_frame = tk.LabelFrame(
            reminders_frame,
            text="My Reminders",
            bg=GUI_THEME_COLOR,
            fg="white"
        )
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        reminders_listbox = tk.Listbox(
            list_frame,
            bg="#34495E",
            fg="white"
        )
        reminders_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Populate reminders
        for reminder in list_all_reminders():
            reminders_listbox.insert(tk.END, f"{reminder['title']} - {reminder['remind_time']}")
        
        # Buttons
        button_frame = tk.Frame(reminders_frame, bg=GUI_THEME_COLOR)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(
            button_frame,
            text="Add Reminder",
            bg=GUI_ACCENT_COLOR,
            fg="white"
        ).pack(side=tk.LEFT, padx=5)
    
    def create_settings_tab(self, notebook):
        """Create settings tab."""
        settings_frame = tk.Frame(notebook, bg=GUI_THEME_COLOR)
        notebook.add(settings_frame, text="Settings")
        
        # About
        about_label = tk.Label(
            settings_frame,
            text=f"{APP_NAME} v{APP_VERSION}",
            font=("Arial", 12, "bold"),
            bg=GUI_THEME_COLOR,
            fg="white"
        )
        about_label.pack(pady=20)
        
        info_label = tk.Label(
            settings_frame,
            text="A professional Python-based Voice Assistant\nwith advanced features and intuitive interface",
            font=("Arial", 10),
            bg=GUI_THEME_COLOR,
            fg="#BDC3C7"
        )
        info_label.pack(pady=10)
    
    def listen_command(self):
        """Listen for voice command in a separate thread."""
        thread = threading.Thread(target=self._listen_thread)
        thread.daemon = True
        thread.start()
    
    def _listen_thread(self):
        """Thread function for listening."""
        try:
            messagebox.showinfo("Listening", "Listening for your command... (speak now)")
            command = listen()
            if command:
                messagebox.showinfo("Recognized", f"I heard: {command}")
                # Process the command through the command processor
                executed, response = self.command_processor.process_command(command)
                messagebox.showinfo("Response", response)
            else:
                messagebox.showwarning("No Input", "Sorry, I didn't hear anything. Please try again.")
        except Exception as e:
            logger.error(f"Error in listen_command: {e}")
            messagebox.showerror("Error", f"An error occurred while listening: {str(e)}")
    
    def speak_demo(self):
        """Demonstrate text-to-speech."""
        speak("Hello! I am your Voice Assistant. How can I help you today?")
    
    def show_weather(self):
        """Show weather information."""
        success, data = get_weather()
        if success:
            message = format_weather_message(data)
            messagebox.showinfo("Weather", message)
        else:
            messagebox.showerror("Weather Error", data)
    
    def show_joke(self):
        """Show a random joke."""
        joke = get_random_joke()
        messagebox.showinfo("Joke", joke)
        speak(joke)


def run_gui():
    """Run the Tkinter GUI."""
    root = tk.Tk()
    gui = VoiceAssistantGUI(root)
    logger.info("Starting GUI application")
    root.mainloop()


if __name__ == "__main__":
    run_gui()
