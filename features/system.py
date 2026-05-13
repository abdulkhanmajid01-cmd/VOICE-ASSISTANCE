"""
System Operations Features Module
Handles PC operations like opening applications, shutdown, etc.
"""

import os
import logging
import subprocess
import psutil
from core.utils import open_application
from config import APPLICATIONS, DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def open_app(app_name):
    """
    Open an application.
    
    Args:
        app_name (str): Name of the application
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        if open_application(app_name):
            logger.info(f"Opened application: {app_name}")
            return True, f"Opening {app_name}"
        else:
            return False, f"I couldn't open {app_name}."
    except Exception as e:
        logger.error(f"Error opening application: {e}")
        return False, "An error occurred while opening the application."


def shutdown_pc():
    """
    Shutdown the PC.
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        logger.warning("Shutdown command initiated")
        if os.name == 'nt':  # Windows
            os.system("shutdown /s /t 30")  # 30 seconds delay
            return True, "Shutting down the PC in 30 seconds."
        else:  # Linux/Mac
            os.system("shutdown -h 1")  # 1 minute delay
            return True, "Shutting down the PC in 1 minute."
    except Exception as e:
        logger.error(f"Error shutting down PC: {e}")
        return False, "I couldn't shutdown the PC."


def restart_pc():
    """
    Restart the PC.
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        logger.warning("Restart command initiated")
        if os.name == 'nt':  # Windows
            os.system("shutdown /r /t 30")  # 30 seconds delay
            return True, "Restarting the PC in 30 seconds."
        else:  # Linux/Mac
            os.system("shutdown -r 1")  # 1 minute delay
            return True, "Restarting the PC in 1 minute."
    except Exception as e:
        logger.error(f"Error restarting PC: {e}")
        return False, "I couldn't restart the PC."


def lock_screen():
    """
    Lock the screen.
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        if os.name == 'nt':  # Windows
            os.system("rundll32.exe user32.dll,LockWorkStation")
            logger.info("Screen locked")
            return True, "Locking the screen."
        else:
            logger.warning("Screen lock not supported on this system")
            return False, "Screen lock is not supported on this system."
    except Exception as e:
        logger.error(f"Error locking screen: {e}")
        return False, "I couldn't lock the screen."


def get_cpu_usage():
    """
    Get CPU usage percentage.
    
    Returns:
        float: CPU usage percentage
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        logger.info(f"CPU usage: {cpu_usage}%")
        return cpu_usage
    except Exception as e:
        logger.error(f"Error getting CPU usage: {e}")
        return 0.0


def get_memory_usage():
    """
    Get memory (RAM) usage percentage.
    
    Returns:
        float: Memory usage percentage
    """
    try:
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        logger.info(f"Memory usage: {memory_usage}%")
        return memory_usage
    except Exception as e:
        logger.error(f"Error getting memory usage: {e}")
        return 0.0


def get_disk_usage():
    """
    Get disk usage percentage.
    
    Returns:
        float: Disk usage percentage
    """
    try:
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent
        logger.info(f"Disk usage: {disk_usage}%")
        return disk_usage
    except Exception as e:
        logger.error(f"Error getting disk usage: {e}")
        return 0.0


def get_available_applications():
    """
    Get list of available applications.
    
    Returns:
        list: List of application names
    """
    return list(APPLICATIONS.keys())


def get_running_processes():
    """
    Get list of running processes.
    
    Returns:
        list: List of process names
    """
    try:
        processes = [proc.name() for proc in psutil.process_iter(['name'])]
        logger.info(f"Retrieved {len(processes)} running processes")
        return processes
    except Exception as e:
        logger.error(f"Error getting running processes: {e}")
        return []


def kill_process(process_name):
    """
    Kill a running process.
    
    Args:
        process_name (str): Name of the process to kill
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Find and kill the process
        found = False
        for proc in psutil.process_iter(['name']):
            if proc.name().lower() == process_name.lower():
                proc.kill()
                found = True
                logger.warning(f"Killed process: {process_name}")
        
        if found:
            return True, f"Closed {process_name}"
        else:
            return False, f"{process_name} is not running."
    except Exception as e:
        logger.error(f"Error killing process: {e}")
        return False, f"I couldn't close {process_name}."
