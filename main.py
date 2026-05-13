"""
Voice Assistant - Main Entry Point
A professional Python-based Voice Assistant with advanced features

Author: Your Name
Version: 2.0.0
License: MIT

This is the main entry point for the Voice Assistant application.
It provides both CLI and GUI interfaces for interacting with the assistant.

Usage:
    python main.py              # Interactive CLI mode
    python main.py --gui        # GUI mode
    python main.py --continuous # Continuous listening mode
"""

import sys
import argparse
import logging
from pathlib import Path

# Ensure logs directory exists
log_dir = Path('data/logs')
log_dir.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data/logs/assistant.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Import configuration and modules
from config import APP_NAME, APP_VERSION, ENABLE_GUI, ENABLE_CHATBOT
from core.commands import get_command_processor
from core.speech_engine import get_speech_engine, listen, speak
from features.conversation import get_greeting, get_farewell
from gui.assistant_gui import run_gui


def print_banner():
    """Print welcome banner."""
    banner = f"""
    ╔═══════════════════════════════════════════╗
    ║     {APP_NAME.upper()} v{APP_VERSION}           ║
    ║   Professional Python Voice Assistant    ║
    ╚═══════════════════════════════════════════╝
    
    Welcome! I'm here to help you with:
    • Web search and browsing
    • Weather updates
    • Time and date information
    • Music playback
    • Note taking
    • Reminders and alarms
    • Application launching
    • System information
    • And much more!
    
    Type 'help' for commands or 'exit' to quit.
    """
    print(banner)


def show_help():
    """Show available commands."""
    help_text = """
    ┌─ VOICE ASSISTANT COMMANDS ─┐
    
    ✓ TIME & DATE:
      "What's the time?" | "Tell me the date"
    
    ✓ WEB BROWSING:
      "Open Google" | "Search YouTube for [query]"
      "Visit Wikipedia" | "Google [query]"
    
    ✓ INFORMATION:
      "What's the weather?" | "How's the weather"
      "Wikipedia search [topic]"
    
    ✓ MUSIC:
      "Play music" | "Stop music"
      "List my music"
    
    ✓ APPLICATIONS:
      "Open Notepad" | "Open Calculator"
      "Open Chrome" | "Open Firefox"
    
    ✓ SYSTEM:
      "CPU usage" | "System usage"
      "Lock screen" | "Shutdown"
    
    ✓ NOTES:
      "Save note [content]" | "Show notes"
      "Read my notes"
    
    ✓ REMINDERS:
      "Set reminder [text]" | "Show reminders"
      "Check upcoming reminders"
    
    ✓ CONVERSATION:
      "Hello" | "How are you?"
      "Tell me a joke" | "What's your name?"
    
    ✓ SPECIAL:
      "help" - Show this help menu
      "exit" / "bye" - Exit the application
    
    └──────────────────────────┘
    """
    print(help_text)


def interactive_mode():
    """
    Run the assistant in interactive CLI mode.
    User types commands instead of speaking.
    """
    logger.info("Starting in interactive mode")
    print_banner()
    
    processor = get_command_processor()
    speech_engine = get_speech_engine()
    
    print(f"\n{get_greeting()}\n")
    
    try:
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Special commands
                if user_input.lower() == "help":
                    show_help()
                    continue
                
                if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                    print(f"\nAssistant: {get_farewell()}")
                    logger.info("User exited application")
                    break
                
                # Process command
                executed, response = processor.process_command(user_input)
                print(f"Assistant: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\nAssistant: {get_farewell()}")
                logger.info("Interrupted by user")
                break
            except Exception as e:
                logger.error(f"Error in interactive mode: {e}")
                print(f"Assistant: An error occurred. {e}\n")
    
    except Exception as e:
        logger.critical(f"Fatal error in interactive mode: {e}")
        print(f"Fatal Error: {e}")


def voice_mode():
    """
    Run the assistant in continuous voice listening mode.
    Assistant listens for voice commands continuously.
    """
    logger.info("Starting in voice listening mode")
    print_banner()
    
    try:
        processor = get_command_processor()
        processor.handle_continuous_listening()
    except Exception as e:
        logger.error(f"Error in voice mode: {e}")
        print(f"Error: {e}")


def single_voice_mode():
    """
    Run the assistant for a single voice command.
    Useful for testing and quick commands.
    """
    logger.info("Starting in single voice command mode")
    print(f"{APP_NAME} v{APP_VERSION} - Ready for voice command\n")
    
    try:
        processor = get_command_processor()
        executed, response, command = processor.handle_single_command()
        
        if command:
            print(f"You: {command}")
            print(f"Assistant: {response}\n")
        else:
            print("No command recognized.")
    
    except Exception as e:
        logger.error(f"Error in single voice mode: {e}")
        print(f"Error: {e}")


def gui_mode():
    """Run the assistant with GUI interface."""
    logger.info("Starting in GUI mode")
    try:
        run_gui()
    except Exception as e:
        logger.error(f"Error in GUI mode: {e}")
        print(f"Error: {e}")


def demo_mode():
    """
    Run a demonstration of the assistant features.
    Shows various capabilities without user input.
    """
    logger.info("Starting in demo mode")
    print_banner()
    
    speech_engine = get_speech_engine()
    
    print("Starting demonstration...\n")
    
    # Demo greeting
    print("Demo: Testing greeting")
    speech_engine.speak(get_greeting())
    print()
    
    # Demo commands
    demo_commands = [
        "What's the time?",
        "Tell me the date",
        "Tell me a joke",
    ]
    
    processor = get_command_processor()
    
    for command in demo_commands:
        print(f"Testing command: {command}")
        executed, response = processor.process_command(command)
        print(f"Response: {response}\n")
    
    print("Demo completed!")


def main():
    """
    Main function - Parse arguments and run appropriate mode.
    """
    parser = argparse.ArgumentParser(
        description=f"{APP_NAME} v{APP_VERSION} - Python Voice Assistant",
        epilog="For more information, visit the documentation"
    )
    
    parser.add_argument(
        '--mode',
        choices=['interactive', 'voice', 'gui', 'demo', 'single'],
        default='interactive',
        help='Execution mode (default: interactive)'
    )
    
    parser.add_argument(
        '--gui',
        action='store_true',
        help='Run in GUI mode'
    )
    
    parser.add_argument(
        '--voice',
        action='store_true',
        help='Run in continuous voice listening mode'
    )
    
    parser.add_argument(
        '--continuous',
        action='store_true',
        help='Run in continuous listening mode (same as --voice)'
    )
    
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run in demo mode'
    )
    
    parser.add_argument(
        '--single',
        action='store_true',
        help='Listen for a single voice command'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f"{APP_NAME} {APP_VERSION}"
    )
    
    parser.add_argument(
        '--help-commands',
        action='store_true',
        help='Show available voice commands'
    )
    
    args = parser.parse_args()
    
    # Show help if requested
    if args.help_commands:
        show_help()
        return
    
    logger.info(f"Starting {APP_NAME} v{APP_VERSION}")
    
    # Determine mode
    if args.gui or (ENABLE_GUI and args.mode == 'gui'):
        gui_mode()
    elif args.voice or args.continuous or args.mode == 'voice':
        voice_mode()
    elif args.single or args.mode == 'single':
        single_voice_mode()
    elif args.demo or args.mode == 'demo':
        demo_mode()
    else:  # Default to interactive mode
        interactive_mode()
    
    logger.info(f"{APP_NAME} shutdown complete")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
        print("\nGoodbye!")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Unhandled exception: {e}")
        print(f"Critical Error: {e}")
        sys.exit(1)
