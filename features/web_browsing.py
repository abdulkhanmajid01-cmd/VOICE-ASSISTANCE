"""
Web Browsing Features Module
Handles opening websites and web searches
"""

import logging
from core.utils import open_website, search_google, search_youtube, extract_query_from_command
from config import WEBSITES, DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def open_website_command(command):
    """
    Open a website based on command.
    
    Args:
        command (str): Voice command
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Extract website name from command
        keywords = ["open", "go to", "visit", "browse"]
        website_name = ""
        
        for keyword in keywords:
            if keyword in command.lower():
                website_name = extract_query_from_command(command, keyword)
                break
        
        if not website_name:
            return False, "Please specify which website you want to open."
        
        website_name = website_name.strip()
        
        if open_website(website_name):
            logger.info(f"Opened website: {website_name}")
            return True, f"Opening {website_name}"
        else:
            return False, f"I couldn't open {website_name}."
    except Exception as e:
        logger.error(f"Error in open_website_command: {e}")
        return False, "An error occurred while opening the website."


def search_google_command(command):
    """
    Search Google based on command.
    
    Args:
        command (str): Voice command
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        query = extract_query_from_command(command, "search google for")
        if not query:
            query = extract_query_from_command(command, "google")
        
        if not query:
            return False, "What would you like me to search for?"
        
        if search_google(query):
            logger.info(f"Searched Google: {query}")
            return True, f"Searching Google for {query}"
        else:
            return False, "I couldn't perform the search."
    except Exception as e:
        logger.error(f"Error in search_google_command: {e}")
        return False, "An error occurred during the search."


def search_youtube_command(command):
    """
    Search YouTube based on command.
    
    Args:
        command (str): Voice command
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        query = extract_query_from_command(command, "search youtube for")
        if not query:
            query = extract_query_from_command(command, "youtube")
        
        if not query:
            return False, "What would you like me to search for?"
        
        if search_youtube(query):
            logger.info(f"Searched YouTube: {query}")
            return True, f"Searching YouTube for {query}"
        else:
            return False, "I couldn't perform the search."
    except Exception as e:
        logger.error(f"Error in search_youtube_command: {e}")
        return False, "An error occurred during the search."


def get_available_websites():
    """
    Get list of available predefined websites.
    
    Returns:
        list: List of website names
    """
    return list(WEBSITES.keys())


def is_url_valid(url):
    """
    Validate if a string is a valid URL.
    
    Args:
        url (str): URL to validate
        
    Returns:
        bool: True if valid URL, False otherwise
    """
    try:
        from urllib.parse import urlparse
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception as e:
        logger.error(f"Error validating URL: {e}")
        return False
