"""
Reminders and Alarms Module
Handles reminders, alarms, and scheduled notifications
"""

import os
import json
import logging
from datetime import datetime, timedelta
from config import REMINDERS_DIR, DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)

REMINDERS_FILE = REMINDERS_DIR / "reminders.json"


def load_reminders():
    """
    Load all reminders from file.
    
    Returns:
        list: List of reminder dictionaries
    """
    try:
        if not REMINDERS_FILE.exists():
            return []
        
        with open(REMINDERS_FILE, 'r', encoding='utf-8') as f:
            reminders = json.load(f)
        
        logger.info(f"Loaded {len(reminders)} reminders")
        return reminders
    except Exception as e:
        logger.error(f"Error loading reminders: {e}")
        return []


def save_reminders(reminders):
    """
    Save reminders to file.
    
    Args:
        reminders (list): List of reminder dictionaries
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(REMINDERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(reminders, f, indent=4)
        
        logger.info(f"Saved {len(reminders)} reminders")
        return True
    except Exception as e:
        logger.error(f"Error saving reminders: {e}")
        return False


def add_reminder(title, description, remind_time):
    """
    Add a new reminder.
    
    Args:
        title (str): Reminder title
        description (str): Reminder description
        remind_time (str): Time to remind (ISO format or relative like "5 minutes")
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        reminders = load_reminders()
        
        # Parse remind_time
        if "minute" in remind_time.lower():
            minutes = int(remind_time.split()[0])
            remind_datetime = datetime.now() + timedelta(minutes=minutes)
        elif "hour" in remind_time.lower():
            hours = int(remind_time.split()[0])
            remind_datetime = datetime.now() + timedelta(hours=hours)
        else:
            remind_datetime = datetime.fromisoformat(remind_time)
        
        reminder = {
            "id": len(reminders) + 1,
            "title": title,
            "description": description,
            "remind_time": remind_datetime.isoformat(),
            "created_at": datetime.now().isoformat(),
            "completed": False,
        }
        
        reminders.append(reminder)
        save_reminders(reminders)
        
        logger.info(f"Reminder added: {title}")
        return True, f"Reminder '{title}' set for {remind_datetime.strftime('%I:%M %p')}"
    except Exception as e:
        logger.error(f"Error adding reminder: {e}")
        return False, "I couldn't set the reminder."


def get_upcoming_reminders(hours=24):
    """
    Get reminders scheduled in the next N hours.
    
    Args:
        hours (int): Number of hours to look ahead
        
    Returns:
        list: List of upcoming reminders
    """
    try:
        reminders = load_reminders()
        now = datetime.now()
        upcoming_time = now + timedelta(hours=hours)
        
        upcoming = []
        for reminder in reminders:
            if not reminder['completed']:
                remind_time = datetime.fromisoformat(reminder['remind_time'])
                if now <= remind_time <= upcoming_time:
                    upcoming.append(reminder)
        
        logger.info(f"Found {len(upcoming)} upcoming reminders")
        return upcoming
    except Exception as e:
        logger.error(f"Error getting upcoming reminders: {e}")
        return []


def complete_reminder(reminder_id):
    """
    Mark a reminder as completed.
    
    Args:
        reminder_id (int): ID of the reminder
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        reminders = load_reminders()
        
        for reminder in reminders:
            if reminder['id'] == reminder_id:
                reminder['completed'] = True
                save_reminders(reminders)
                logger.info(f"Reminder completed: {reminder_id}")
                return True, f"Reminder '{reminder['title']}' marked as completed."
        
        return False, "Reminder not found."
    except Exception as e:
        logger.error(f"Error completing reminder: {e}")
        return False, "I couldn't complete the reminder."


def delete_reminder(reminder_id):
    """
    Delete a reminder.
    
    Args:
        reminder_id (int): ID of the reminder
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        reminders = load_reminders()
        original_count = len(reminders)
        
        reminders = [r for r in reminders if r['id'] != reminder_id]
        
        if len(reminders) < original_count:
            save_reminders(reminders)
            logger.info(f"Reminder deleted: {reminder_id}")
            return True, "Reminder deleted successfully."
        else:
            return False, "Reminder not found."
    except Exception as e:
        logger.error(f"Error deleting reminder: {e}")
        return False, "I couldn't delete the reminder."


def check_reminders():
    """
    Check if any reminders should be triggered now.
    
    Returns:
        list: List of reminders to trigger
    """
    try:
        reminders = load_reminders()
        now = datetime.now()
        to_trigger = []
        
        for reminder in reminders:
            if not reminder['completed']:
                remind_time = datetime.fromisoformat(reminder['remind_time'])
                # Trigger if within 1 minute window
                if (remind_time - timedelta(minutes=1)) <= now <= remind_time:
                    to_trigger.append(reminder)
        
        logger.info(f"Checking reminders: {len(to_trigger)} to trigger")
        return to_trigger
    except Exception as e:
        logger.error(f"Error checking reminders: {e}")
        return []


def set_alarm(alarm_time, message="Alarm!"):
    """
    Set an alarm for a specific time.
    
    Args:
        alarm_time (str): Time for the alarm (ISO format)
        message (str): Message to play when alarm rings
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        title = f"Alarm - {message}"
        description = message
        
        return add_reminder(title, description, alarm_time)
    except Exception as e:
        logger.error(f"Error setting alarm: {e}")
        return False, "I couldn't set the alarm."


def list_all_reminders():
    """
    List all reminders.
    
    Returns:
        list: List of all reminders
    """
    try:
        reminders = load_reminders()
        logger.info(f"Listed {len(reminders)} reminders")
        return reminders
    except Exception as e:
        logger.error(f"Error listing reminders: {e}")
        return []
