"""
Time and Date Features Module
Handles current time, date, and scheduling features
"""

from datetime import datetime, timedelta
import logging
from core.utils import format_time, format_date
from config import DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def get_current_time():
    """
    Get and speak the current time.
    
    Returns:
        str: Formatted current time
    """
    try:
        current_time = datetime.now()
        time_string = format_time(current_time)
        logger.info(f"Retrieved current time: {time_string}")
        return f"The current time is {time_string}"
    except Exception as e:
        logger.error(f"Error getting current time: {e}")
        return "I couldn't retrieve the current time."


def get_current_date():
    """
    Get and speak the current date.
    
    Returns:
        str: Formatted current date
    """
    try:
        current_date = datetime.now()
        date_string = format_date(current_date)
        logger.info(f"Retrieved current date: {date_string}")
        return f"Today is {date_string}"
    except Exception as e:
        logger.error(f"Error getting current date: {e}")
        return "I couldn't retrieve the current date."


def get_day_of_week():
    """
    Get the current day of the week.
    
    Returns:
        str: Current day of the week
    """
    try:
        day = datetime.now().strftime("%A")
        logger.info(f"Retrieved day of week: {day}")
        return f"Today is {day}"
    except Exception as e:
        logger.error(f"Error getting day of week: {e}")
        return "I couldn't determine the day."


def get_time_until_event(event_name, event_date):
    """
    Calculate time until a specific event.
    
    Args:
        event_name (str): Name of the event
        event_date (datetime): Date of the event
        
    Returns:
        str: Time until the event
    """
    try:
        now = datetime.now()
        time_diff = event_date - now
        
        if time_diff.total_seconds() < 0:
            return f"{event_name} has already passed."
        
        days = time_diff.days
        hours = time_diff.seconds // 3600
        minutes = (time_diff.seconds % 3600) // 60
        
        parts = []
        if days > 0:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        
        time_str = ", ".join(parts)
        return f"{time_str} until {event_name}"
    except Exception as e:
        logger.error(f"Error calculating time until event: {e}")
        return "I couldn't calculate the time."


def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    Args:
        year (int): Year to check
        
    Returns:
        bool: True if leap year, False otherwise
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_uptime():
    """
    Get system uptime (basic implementation).
    
    Returns:
        str: System uptime message
    """
    try:
        import psutil
        uptime = timedelta(seconds=psutil.boot_time())
        logger.info(f"System uptime retrieved")
        return f"System uptime: {uptime}"
    except ImportError:
        logger.warning("psutil not installed, cannot get system uptime")
        return "I cannot determine system uptime."
    except Exception as e:
        logger.error(f"Error getting system uptime: {e}")
        return "I couldn't get the system uptime."
