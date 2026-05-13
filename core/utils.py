"""
Utility Functions Module
Contains helper functions used throughout the application
"""

import os
import webbrowser
import subprocess
import logging
from datetime import datetime
from config import APPLICATIONS, WEBSITES, LOGS_DIR, DEBUG_MODE

# Configure logging
logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def open_website(website_name):
    """
    Open a website in the default web browser.
    
    Args:
        website_name (str): Name of the website to open
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        website_name = website_name.lower().strip()
        
        if website_name in WEBSITES:
            url = WEBSITES[website_name]
        else:
            # Try to construct a URL if not in predefined list
            if not website_name.startswith(("http://", "https://")):
                url = f"https://{website_name}.com"
            else:
                url = website_name
        
        webbrowser.open(url)
        logger.info(f"Opened website: {url}")
        return True
    except Exception as e:
        logger.error(f"Error opening website: {e}")
        return False


def open_application(app_name):
    """
    Open an application on the system.
    
    Args:
        app_name (str): Name of the application to open
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        app_name = app_name.lower().strip()
        
        if app_name in APPLICATIONS:
            app_path = APPLICATIONS[app_name]
            if os.path.exists(app_path):
                subprocess.Popen(app_path)
                logger.info(f"Opened application: {app_name}")
                return True
            else:
                logger.warning(f"Application not found: {app_path}")
                return False
        else:
            logger.warning(f"Application not in predefined list: {app_name}")
            return False
    except Exception as e:
        logger.error(f"Error opening application: {e}")
        return False


def search_google(query):
    """
    Search on Google.
    
    Args:
        query (str): Search query
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        logger.info(f"Google search: {query}")
        return True
    except Exception as e:
        logger.error(f"Error searching Google: {e}")
        return False


def search_youtube(query):
    """
    Search on YouTube.
    
    Args:
        query (str): Search query
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        logger.info(f"YouTube search: {query}")
        return True
    except Exception as e:
        logger.error(f"Error searching YouTube: {e}")
        return False


def extract_query_from_command(command, prefix):
    """
    Extract query from a command by removing the prefix.
    
    Example:
        extract_query_from_command("search google for python", "search google for")
        Returns: "python"
    
    Args:
        command (str): The command string
        prefix (str): The prefix to remove
        
    Returns:
        str: The extracted query
    """
    try:
        if command.lower().startswith(prefix.lower()):
            return command[len(prefix):].strip()
        return ""
    except Exception as e:
        logger.error(f"Error extracting query: {e}")
        return ""


def log_activity(activity, details=""):
    """
    Log user activity for debugging and analytics.
    
    Args:
        activity (str): Activity description
        details (str): Additional details
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {activity}"
        if details:
            log_message += f" - {details}"
        logger.info(log_message)
    except Exception as e:
        logger.error(f"Error logging activity: {e}")


def is_internet_connected():
    """
    Check if internet connection is available.
    
    Returns:
        bool: True if connected to internet, False otherwise
    """
    try:
        import urllib.request
        urllib.request.urlopen("http://www.google.com", timeout=2)
        return True
    except Exception:
        return False


def get_system_info():
    """
    Get system information.
    
    Returns:
        dict: Dictionary containing system information
    """
    try:
        import platform
        info = {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        }
        return info
    except Exception as e:
        logger.error(f"Error getting system info: {e}")
        return {}


def format_time(time_obj):
    """
    Format time object to readable string.
    
    Args:
        time_obj: Time object
        
    Returns:
        str: Formatted time string
    """
    try:
        return time_obj.strftime("%I:%M %p")
    except Exception as e:
        logger.error(f"Error formatting time: {e}")
        return ""


def format_date(date_obj):
    """
    Format date object to readable string.
    
    Args:
        date_obj: Date object
        
    Returns:
        str: Formatted date string
    """
    try:
        return date_obj.strftime("%A, %B %d, %Y")
    except Exception as e:
        logger.error(f"Error formatting date: {e}")
        return ""
