"""
Wikipedia Search Features Module
Handles Wikipedia article search and information retrieval
"""

import logging
import wikipedia
from config import DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def search_wikipedia(query):
    """
    Search Wikipedia for a topic.
    
    Args:
        query (str): Search query
        
    Returns:
        tuple: (success: bool, result: str)
    """
    try:
        if not query or len(query.strip()) == 0:
            return False, "Please provide a topic to search."
        
        logger.info(f"Searching Wikipedia for: {query}")
        
        # Set language to English
        wikipedia.set_lang("en")
        
        # Search for the query
        results = wikipedia.search(query)
        
        if not results:
            return False, f"I couldn't find information about {query} on Wikipedia."
        
        try:
            # Get the summary of the first result
            page = wikipedia.page(results[0])
            summary = page.summary[:500]  # Get first 500 characters
            
            logger.info(f"Found Wikipedia article: {page.title}")
            return True, summary
        except wikipedia.exceptions.DisambiguationError as e:
            # If disambiguation page, return list of options
            options = ", ".join(e.options[:5])  # Show first 5 options
            logger.warning(f"Disambiguation page for: {query}")
            return False, f"Did you mean: {options}?"
        except wikipedia.exceptions.PageError:
            return False, f"I couldn't find a page for {query}."
    except Exception as e:
        logger.error(f"Error searching Wikipedia: {e}")
        return False, "An error occurred while searching Wikipedia."


def get_wikipedia_summary(topic):
    """
    Get Wikipedia summary for a topic.
    
    Args:
        topic (str): Topic to get summary for
        
    Returns:
        str: Wikipedia summary
    """
    try:
        wikipedia.set_lang("en")
        page = wikipedia.page(topic)
        summary = page.summary
        logger.info(f"Retrieved Wikipedia summary for: {topic}")
        return summary
    except Exception as e:
        logger.error(f"Error getting Wikipedia summary: {e}")
        return f"I couldn't retrieve information about {topic}."


def get_wikipedia_url(topic):
    """
    Get Wikipedia URL for a topic.
    
    Args:
        topic (str): Topic to get URL for
        
    Returns:
        str: Wikipedia URL or empty string
    """
    try:
        wikipedia.set_lang("en")
        page = wikipedia.page(topic)
        logger.info(f"Retrieved Wikipedia URL for: {topic}")
        return page.url
    except Exception as e:
        logger.error(f"Error getting Wikipedia URL: {e}")
        return ""


def get_wikipedia_page_info(topic):
    """
    Get detailed information about a Wikipedia page.
    
    Args:
        topic (str): Topic to get information for
        
    Returns:
        dict: Dictionary containing page information
    """
    try:
        wikipedia.set_lang("en")
        page = wikipedia.page(topic)
        
        info = {
            "title": page.title,
            "summary": page.summary,
            "url": page.url,
            "links_count": len(page.links),
        }
        
        logger.info(f"Retrieved Wikipedia page info for: {topic}")
        return info
    except Exception as e:
        logger.error(f"Error getting Wikipedia page info: {e}")
        return {}
