"""
Modern GUI Module - Advanced Tkinter Interface with Animations
Provides a sleek, Jarvis-like graphical interface for the Voice Assistant
Features: Dark futuristic theme, animations, smooth interactions, background listening
"""

import tkinter as tk
from tkinter import ttk
import logging
import threading
import math
from datetime import datetime
from config import (
    APP_NAME, APP_VERSION, GUI_THEME_COLOR, GUI_ACCENT_COLOR, GUI_SECONDARY_COLOR,
    GUI_WINDOW_WIDTH, GUI_WINDOW_HEIGHT, DEBUG_MODE, WAKE_WORDS
)
from core.speech_engine import get_speech_engine
from core.commands import get_command_processor
from features.conversation import get_greeting

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


class ModernVoiceAssistantGUI:
    """Modern Tkinter GUI for Voice Assistant with animations and continuous listening"""
    
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.speech_engine = get_speech_engine()
        self.command_processor = get_command_processor()
        
        self.is_listening = False
        self.animation_id = None
        self.listening_thread = None
        self.background_listening_active = False
        
        self.create_widgets()
        self.start_background_listening()
        
        logger.info("Modern GUI initialized")
    
    def setup_window(self):
        """Configure the main window with modern styling"""
        self.root.title(f"{APP_NAME} - Jarvis Edition")
        self.root.geometry(f"{GUI_WINDOW_WIDTH}x{GUI_WINDOW_HEIGHT}")
        self.root.configure(bg=GUI_THEME_COLOR)
        
        # Modern window styling
        self.root.resizable(False, False)
        
        # Center on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create modern GUI widgets with dark theme"""
        # Main container
        main_frame = tk.Frame(self.root, bg=GUI_THEME_COLOR)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Top bar with gradient effect (simulated with color)
        top_bar = tk.Frame(main_frame, bg=GUI_SECONDARY_COLOR, height=60)
        top_bar.pack(fill=tk.X, pady=(0, 20))
        top_bar.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            top_bar,
            text="J A R V I S",
            font=("Arial", 24, "bold"),
            bg=GUI_SECONDARY_COLOR,
            fg=GUI_ACCENT_COLOR
        )
        title_label.pack(pady=10)
        
        # Status indicator
        status_frame = tk.Frame(main_frame, bg=GUI_THEME_COLOR)
        status_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        self.status_dot = tk.Label(
            status_frame,
            text="●",
            font=("Arial", 16),
            fg="#00FF00",
            bg=GUI_THEME_COLOR
        )
        self.status_dot.pack(side=tk.LEFT, padx=(0, 10))
        
        self.status_text = tk.Label(
            status_frame,
            text="🎧 Listening in Background...",
            font=("Arial", 11),
            fg=GUI_ACCENT_COLOR,
            bg=GUI_THEME_COLOR
        )
        self.status_text.pack(side=tk.LEFT)
        
        # Main content area
        content_frame = tk.Frame(main_frame, bg=GUI_THEME_COLOR)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Animated microphone area
        mic_frame = tk.Frame(content_frame, bg=GUI_THEME_COLOR)
        mic_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Canvas for animations
        self.canvas = tk.Canvas(
            mic_frame,
            width=300,
            height=300,
            bg=GUI_THEME_COLOR,
            highlightthickness=0
        )
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        # Voice waves animation canvas
        self.wave_canvas = tk.Canvas(
            mic_frame,
            width=300,
            height=300,
            bg=GUI_THEME_COLOR,
            highlightthickness=0
        )
        self.wave_canvas.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        
        # Draw initial microphone
        self.draw_microphone()
        self.draw_voice_waves()
        
        # Command feedback area
        feedback_frame = tk.LabelFrame(
            content_frame,
            text="Last Command",
            bg=GUI_THEME_COLOR,
            fg=GUI_ACCENT_COLOR,
            font=("Arial", 9, "bold"),
            borderwidth=1,
            relief=tk.SUNKEN
        )
        feedback_frame.pack(fill=tk.X, pady=20)
        
        self.feedback_text = tk.Label(
            feedback_frame,
            text="Waiting for command...",
            font=("Arial", 10),
            fg="#00FF00",
            bg="#1a1a1a",
            wraplength=400,
            justify=tk.LEFT,
            padx=15,
            pady=10
        )
        self.feedback_text.pack(fill=tk.X)
        
        # Bottom control panel
        control_frame = tk.Frame(content_frame, bg=GUI_THEME_COLOR)
        control_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Exit button only - listening button removed
        exit_btn = tk.Button(
            control_frame,
            text="⏹ Exit",
            command=self.shutdown,
            bg="#FF3333",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        exit_btn.pack(side=tk.RIGHT, padx=5)
    
    def draw_microphone(self):
        """Draw animated microphone icon"""
        self.canvas.delete("all")
        
        # Outer glow
        self.canvas.create_oval(
            75, 50, 225, 200,
            fill="",
            outline=GUI_ACCENT_COLOR,
            width=2
        )
        
        # Microphone body
        self.canvas.create_oval(
            100, 70, 200, 170,
            fill=GUI_SECONDARY_COLOR,
            outline=GUI_ACCENT_COLOR,
            width=3
        )
        
        # Microphone stand
        self.canvas.create_rectangle(
            145, 170, 155, 250,
            fill=GUI_ACCENT_COLOR,
            outline=GUI_ACCENT_COLOR,
            width=2
        )
        
        # Base
        self.canvas.create_rectangle(
            120, 250, 180, 260,
            fill=GUI_ACCENT_COLOR,
            outline=GUI_ACCENT_COLOR,
            width=2
        )
        
        # Status text
        self.canvas.create_text(
            150, 280,
            text="AI Assistant",
            font=("Arial", 12, "bold"),
            fill=GUI_ACCENT_COLOR
        )
    
    def draw_voice_waves(self):
        """Draw animated voice wave visualization"""
        self.wave_canvas.delete("all")
        
        # Draw concentric circles for wave effect
        center_x, center_y = 150, 150
        
        # Base circle
        self.wave_canvas.create_oval(
            center_x - 20, center_y - 20,
            center_x + 20, center_y + 20,
            fill=GUI_ACCENT_COLOR,
            outline=GUI_ACCENT_COLOR
        )
        
        # Wave circles
        for i in range(1, 4):
            radius = 40 + (i * 30)
            self.wave_canvas.create_oval(
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius,
                fill="",
                outline=GUI_ACCENT_COLOR,
                width=2
            )
        
        # Wave text
        self.wave_canvas.create_text(
            150, 280,
            text="Background Listen",
            font=("Arial", 10),
            fill=GUI_ACCENT_COLOR
        )
    
    def animate_listening(self):
        """Animate while listening to voice"""
        if self.is_listening:
            self.wave_canvas.delete("all")
            
            center_x, center_y = 150, 150
            
            # Pulsing center
            size = 20 + (math.sin(datetime.now().timestamp() * 10) * 5)
            self.wave_canvas.create_oval(
                center_x - size, center_y - size,
                center_x + size, center_y + size,
                fill=GUI_ACCENT_COLOR,
                outline=GUI_ACCENT_COLOR
            )
            
            # Animated waves
            for i in range(1, 4):
                radius = 40 + (i * 30) + (math.sin(datetime.now().timestamp() * 5 + i) * 10)
                opacity_factor = abs(math.sin(datetime.now().timestamp() * 5 + i))
                
                self.wave_canvas.create_oval(
                    center_x - radius, center_y - radius,
                    center_x + radius, center_y + radius,
                    fill="",
                    outline=GUI_ACCENT_COLOR,
                    width=int(2 * opacity_factor) + 1
                )
            
            self.wave_canvas.create_text(
                150, 280,
                text="Listening...",
                font=("Arial", 10, "bold"),
                fill="#00FF00"
            )
            
            self.animation_id = self.wave_canvas.after(50, self.animate_listening)
    
    def start_background_listening(self):
        """Start background listening thread"""
        if not self.background_listening_active:
            self.background_listening_active = True
            thread = threading.Thread(target=self._background_listen_loop, daemon=True)
            thread.start()
    
    def _background_listen_loop(self):
        """Continuous background listening loop with advanced filtering"""
        logger.info("Background listening started")
        
        while self.background_listening_active:
            try:
                # Faster listening with optimized timeout
                text = self.speech_engine.listen(timeout=5)  # Faster timeout
                
                if text and len(text.strip()) > 2:  # Filter out very short noise
                    # Process any voice command directly (no wake word required)
                    command = text.strip()
                    
                    # Filter out common noise patterns (single letters, numbers, etc.)
                    words = command.split()
                    if len(words) >= 1 and not all(len(word) == 1 for word in words):
                        # Update status
                        self.update_status(f"🎤 Command: {command}", "#00FF00")
                        
                        # Process command in thread
                        self._process_command_thread(command)
                    
            except Exception as e:
                logger.debug(f"Background listening: {e}")
                continue
    
    def _has_wake_word(self, text):
        """Check if text contains any wake word"""
        text_lower = text.lower()
        for wake_word in WAKE_WORDS:
            if wake_word.lower() in text_lower:
                return True
        return False
    
    def _extract_command_after_wake_word(self, text):
        """Extract command after wake word"""
        text_lower = text.lower()
        for wake_word in WAKE_WORDS:
            if wake_word.lower() in text_lower:
                # Get text after wake word
                idx = text_lower.index(wake_word.lower()) + len(wake_word)
                command = text[idx:].strip()
                return command if command else text
        return text
    
    def _process_command_thread(self, command):
        """Process command in separate thread with proper management"""
        thread = threading.Thread(
            target=self._execute_command,
            args=(command,),
            daemon=False  # Non-daemon to ensure proper completion
        )
        thread.start()
    
    def _execute_command(self, command):
        """Execute voice command with guaranteed voice feedback"""
        try:
            self.is_listening = True
            self.animate_listening()
            
            # Process command (this already calls TTS internally)
            executed, response = self.command_processor.process_command(command)
            
            self.is_listening = False
            self.update_status(f"✓ {response}", GUI_ACCENT_COLOR)
            logger.info(f"Executed: {command} -> {response}")
            
            # Return to background listening after response completes
            self.root.after(3000, lambda: self.update_status("🎧 Listening in Background...", GUI_ACCENT_COLOR))
            
        except Exception as e:
            logger.error(f"Error executing command: {e}")
            self.is_listening = False
            self.update_status(f"✗ Error: {str(e)[:50]}", "#FF6666")
    
    def update_status(self, text, color):
        """Update status text and color"""
        self.root.after(0, lambda: self._update_status_sync(text, color))
    
    def _update_status_sync(self, text, color):
        """Synchronous status update"""
        try:
            self.feedback_text.config(text=text, fg=color)
            self.status_text.config(text=text, fg=color)
        except tk.TclError:
            pass
    
    def shutdown(self):
        """Clean shutdown"""
        logger.info("Shutting down assistant")
        self.background_listening_active = False
        
        if self.animation_id:
            self.root.after_cancel(self.animation_id)
        
        try:
            self.speech_engine.close()
        except Exception as e:
            logger.debug(f"Error closing speech engine: {e}")
        
        self.root.quit()
    
    def on_closing(self):
        """Handle window closing"""
        self.shutdown()


def run_modern_gui():
    """Run the modern GUI"""
    root = tk.Tk()
    gui = ModernVoiceAssistantGUI(root)
    
    root.protocol("WM_DELETE_WINDOW", gui.on_closing)
    logger.info("Starting Modern GUI application")
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        gui.shutdown()
    except Exception as e:
        logger.error(f"GUI Error: {e}")
        gui.shutdown()


if __name__ == "__main__":
    run_modern_gui()
