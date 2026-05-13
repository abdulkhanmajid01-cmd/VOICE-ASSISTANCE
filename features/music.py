"""
Music Player Features Module
Handles music playback functionality
"""

import os
import logging
import subprocess
from config import MUSIC_FOLDERS, SUPPORTED_FORMATS, DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def find_music_files():
    """
    Find all music files in configured folders.
    
    Returns:
        list: List of music file paths
    """
    try:
        music_files = []
        
        for folder in MUSIC_FOLDERS:
            if os.path.exists(folder):
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    if os.path.isfile(file_path):
                        _, ext = os.path.splitext(filename)
                        if ext.lower() in SUPPORTED_FORMATS:
                            music_files.append(file_path)
        
        logger.info(f"Found {len(music_files)} music files")
        return music_files
    except Exception as e:
        logger.error(f"Error finding music files: {e}")
        return []


def play_music(music_file=None):
    """
    Play a music file.
    
    Args:
        music_file (str): Path to music file. If None, plays a random file.
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        if music_file is None:
            # Find and play a random music file
            music_files = find_music_files()
            if not music_files:
                return False, "No music files found."
            
            import random
            music_file = random.choice(music_files)
        
        if not os.path.exists(music_file):
            return False, "Music file not found."
        
        # Use Windows Media Player or default player
        try:
            if os.name == 'nt':  # Windows
                os.startfile(music_file)
            else:
                subprocess.Popen(['xdg-open', music_file])
            
            filename = os.path.basename(music_file)
            logger.info(f"Playing music: {filename}")
            return True, f"Playing {filename}"
        except Exception as e:
            logger.error(f"Error playing music: {e}")
            return False, "I couldn't play the music file."
    except Exception as e:
        logger.error(f"Error in play_music: {e}")
        return False, "An error occurred while playing music."


def stop_music():
    """
    Stop music playback.
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # This is a placeholder - stopping media depends on the player
        logger.info("Stop music requested")
        return True, "Stopping music"
    except Exception as e:
        logger.error(f"Error stopping music: {e}")
        return False, "I couldn't stop the music."


def get_music_info(music_file):
    """
    Get information about a music file.
    
    Args:
        music_file (str): Path to music file
        
    Returns:
        dict: Dictionary with file information
    """
    try:
        info = {
            "filename": os.path.basename(music_file),
            "size": os.path.getsize(music_file),
            "path": music_file,
        }
        logger.info(f"Retrieved music file info: {music_file}")
        return info
    except Exception as e:
        logger.error(f"Error getting music file info: {e}")
        return {}


def list_music_files():
    """
    List all available music files.
    
    Returns:
        list: List of music file names
    """
    try:
        music_files = find_music_files()
        filenames = [os.path.basename(f) for f in music_files]
        logger.info(f"Listed {len(filenames)} music files")
        return filenames
    except Exception as e:
        logger.error(f"Error listing music files: {e}")
        return []
