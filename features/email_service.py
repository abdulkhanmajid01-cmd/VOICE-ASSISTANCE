"""
Email Services Module
Handles sending and receiving emails
"""

import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def send_email(to_address, subject, body):
    """
    Send an email.
    
    Args:
        to_address (str): Recipient email address
        subject (str): Email subject
        body (str): Email body
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        if EMAIL_ADDRESS == "your_email@gmail.com" or EMAIL_PASSWORD == "your_app_password":
            logger.warning("Email credentials not configured")
            return False, "Email service is not configured. Please set your email credentials in config.py"
        
        logger.info(f"Preparing to send email to: {to_address}")
        
        # Create email message
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = to_address
        message['Subject'] = subject
        
        # Attach body
        message.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
        
        logger.info(f"Email sent to: {to_address}")
        return True, f"Email sent to {to_address}"
    except smtplib.SMTPAuthenticationError:
        logger.error("Email authentication failed")
        return False, "Email authentication failed. Check your credentials."
    except Exception as e:
        logger.error(f"Error sending email: {e}")
        return False, "I couldn't send the email."


def send_reminder_email(recipient, reminder_message):
    """
    Send a reminder email.
    
    Args:
        recipient (str): Recipient email address
        reminder_message (str): Reminder message
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        subject = "Voice Assistant Reminder"
        body = f"This is a reminder from your Voice Assistant:\n\n{reminder_message}"
        
        return send_email(recipient, subject, body)
    except Exception as e:
        logger.error(f"Error sending reminder email: {e}")
        return False, "I couldn't send the reminder email."


def validate_email(email_address):
    """
    Validate email address format.
    
    Args:
        email_address (str): Email address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid = re.match(pattern, email_address) is not None
        logger.debug(f"Email validation for {email_address}: {is_valid}")
        return is_valid
    except Exception as e:
        logger.error(f"Error validating email: {e}")
        return False


def get_email_domain(email_address):
    """
    Extract domain from email address.
    
    Args:
        email_address (str): Email address
        
    Returns:
        str: Domain name
    """
    try:
        domain = email_address.split('@')[1] if '@' in email_address else ""
        logger.debug(f"Extracted domain: {domain}")
        return domain
    except Exception as e:
        logger.error(f"Error extracting domain: {e}")
        return ""


def is_email_configured():
    """
    Check if email service is properly configured.
    
    Returns:
        bool: True if configured, False otherwise
    """
    return (EMAIL_ADDRESS != "your_email@gmail.com" and 
            EMAIL_PASSWORD != "your_app_password")
