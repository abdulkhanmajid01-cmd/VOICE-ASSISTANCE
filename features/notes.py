"""
Notes Features Module
Handles note taking and file management
"""

import os
import logging
from datetime import datetime
from config import NOTES_DIR, DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def save_note(title, content):
    """
    Save a note to a file.
    
    Args:
        title (str): Title of the note
        content (str): Content of the note
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Create filename from title
        filename = f"{title.replace(' ', '_')}.txt"
        filepath = NOTES_DIR / filename
        
        # Add timestamp to content
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_content = f"Title: {title}\nDate: {timestamp}\n\n{content}\n"
        
        # Write to file
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(full_content)
        
        logger.info(f"Note saved: {filepath}")
        return True, f"Note '{title}' saved successfully."
    except Exception as e:
        logger.error(f"Error saving note: {e}")
        return False, "I couldn't save the note."


def read_note(title):
    """
    Read a note from file.
    
    Args:
        title (str): Title of the note
        
    Returns:
        tuple: (success: bool, content: str)
    """
    try:
        filename = f"{title.replace(' ', '_')}.txt"
        filepath = NOTES_DIR / filename
        
        if not filepath.exists():
            return False, f"Note '{title}' not found."
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        logger.info(f"Note read: {filepath}")
        return True, content
    except Exception as e:
        logger.error(f"Error reading note: {e}")
        return False, "I couldn't read the note."


def list_notes():
    """
    List all saved notes.
    
    Returns:
        list: List of note titles
    """
    try:
        notes = []
        for file in os.listdir(NOTES_DIR):
            if file.endswith('.txt'):
                title = file.replace('_', ' ').replace('.txt', '')
                notes.append(title)
        
        logger.info(f"Listed {len(notes)} notes")
        return notes
    except Exception as e:
        logger.error(f"Error listing notes: {e}")
        return []


def delete_note(title):
    """
    Delete a note.
    
    Args:
        title (str): Title of the note
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        filename = f"{title.replace(' ', '_')}.txt"
        filepath = NOTES_DIR / filename
        
        if not filepath.exists():
            return False, f"Note '{title}' not found."
        
        os.remove(filepath)
        logger.info(f"Note deleted: {filepath}")
        return True, f"Note '{title}' deleted successfully."
    except Exception as e:
        logger.error(f"Error deleting note: {e}")
        return False, "I couldn't delete the note."


def search_notes(keyword):
    """
    Search for notes containing a keyword.
    
    Args:
        keyword (str): Keyword to search for
        
    Returns:
        list: List of matching note titles
    """
    try:
        matching_notes = []
        keyword_lower = keyword.lower()
        
        for file in os.listdir(NOTES_DIR):
            if file.endswith('.txt'):
                filepath = NOTES_DIR / file
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                
                if keyword_lower in content:
                    title = file.replace('_', ' ').replace('.txt', '')
                    matching_notes.append(title)
        
        logger.info(f"Found {len(matching_notes)} notes matching '{keyword}'")
        return matching_notes
    except Exception as e:
        logger.error(f"Error searching notes: {e}")
        return []


def export_notes(export_path):
    """
    Export all notes to a file.
    
    Args:
        export_path (str): Path to export file
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        with open(export_path, 'w', encoding='utf-8') as export_file:
            for file in os.listdir(NOTES_DIR):
                if file.endswith('.txt'):
                    filepath = NOTES_DIR / file
                    with open(filepath, 'r', encoding='utf-8') as note_file:
                        export_file.write(note_file.read())
                    export_file.write("\n" + "="*50 + "\n\n")
        
        logger.info(f"Notes exported to: {export_path}")
        return True, f"Notes exported to {export_path}"
    except Exception as e:
        logger.error(f"Error exporting notes: {e}")
        return False, "I couldn't export the notes."
