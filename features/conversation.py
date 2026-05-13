"""
Conversation Features Module
Handles basic conversation and AI chatbot integration
"""

import logging
import random
from config import (
    GREETING_RESPONSES, FAREWELL_RESPONSES, CONFUSED_RESPONSES,
    DEBUG_MODE
)

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def get_greeting():
    """
    Get a random greeting response.
    
    Returns:
        str: Random greeting
    """
    greeting = random.choice(GREETING_RESPONSES)
    logger.info("Greeting provided")
    return greeting


def get_farewell():
    """
    Get a random farewell response.
    
    Returns:
        str: Random farewell
    """
    farewell = random.choice(FAREWELL_RESPONSES)
    logger.info("Farewell provided")
    return farewell


def get_confused_response():
    """
    Get a random confused response.
    
    Returns:
        str: Random confused response
    """
    response = random.choice(CONFUSED_RESPONSES)
    logger.info("Confused response provided")
    return response


def chat_with_api(user_input):
    """
    Chat with an AI API (requires internet connection).
    Uses a simple approach without API keys for demonstration.
    
    Args:
        user_input (str): User's message
        
    Returns:
        str: AI response
    """
    try:
        # This is a placeholder for AI chatbot integration
        # You can integrate with services like:
        # - OpenAI API (ChatGPT)
        # - Google Bard API
        # - Hugging Face API
        # - Local AI models
        
        logger.info(f"Chat request: {user_input}")
        
        # Simple pattern matching for common questions
        user_input_lower = user_input.lower()
        
        responses = {
            "how are you": "I'm doing well, thank you for asking! How can I help you today?",
            "what is your name": "I'm Voice Assistant, your personal AI helper.",
            "what can you do": "I can help you with web searches, weather, time, notes, and much more!",
            "tell me a joke": get_random_joke(),
            "what is the meaning of life": "The meaning of life is what you make of it!",
        }
        
        # Check for matching patterns
        for key, value in responses.items():
            if key in user_input_lower:
                logger.info(f"Pattern matched: {key}")
                return value
        
        # If no pattern matches, return a generic response
        return "That's interesting! Tell me more about that."
    
    except Exception as e:
        logger.error(f"Error in chat_with_api: {e}")
        return "I couldn't understand that. Could you rephrase?"


def get_random_joke():
    """
    Get a random joke.
    
    Returns:
        str: Random joke
    """
    jokes = [
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why do Java developers wear glasses? Because they don't C#.",
        "What's a programmer's favorite place to hang out? Stack Overflow.",
        "Why did the Python programmer refuse to play hide and seek? Because good Python code should be visible.",
    ]
    
    joke = random.choice(jokes)
    logger.info("Joke provided")
    return joke


def respond_to_statement(statement):
    """
    Generate a response to a user statement.
    
    Args:
        statement (str): User's statement
        
    Returns:
        str: Response to the statement
    """
    try:
        statement_lower = statement.lower()
        
        # Simple response generation
        if any(word in statement_lower for word in ["thanks", "thank you", "appreciate"]):
            return "You're welcome! I'm always here to help."
        elif any(word in statement_lower for word in ["sorry", "apologize"]):
            return "No problem at all! It happens to everyone."
        elif any(word in statement_lower for word in ["good morning", "good afternoon", "good evening"]):
            return "Good time of day to you too!"
        else:
            return chat_with_api(statement)
    
    except Exception as e:
        logger.error(f"Error responding to statement: {e}")
        return get_confused_response()


def ask_yes_no_question(question):
    """
    Ask a yes/no question and interpret response.
    
    Args:
        question (str): Question to ask
        
    Returns:
        tuple: (success: bool, answer: bool or None)
    """
    try:
        logger.info(f"Yes/No question: {question}")
        # This would be used with the speech engine to ask the user
        # For now, returning a placeholder
        return True, None
    except Exception as e:
        logger.error(f"Error asking question: {e}")
        return False, None


def interpret_yes_no_response(response):
    """
    Interpret if a response is yes or no.
    
    Args:
        response (str): User's response
        
    Returns:
        bool or None: True for yes, False for no, None for unclear
    """
    try:
        response_lower = response.lower().strip()
        
        yes_words = ["yes", "yeah", "yep", "sure", "okay", "ok", "affirmative", "correct"]
        no_words = ["no", "nope", "nah", "negative", "false", "don't", "dont"]
        
        if any(word in response_lower for word in yes_words):
            logger.info("Response interpreted as: YES")
            return True
        elif any(word in response_lower for word in no_words):
            logger.info("Response interpreted as: NO")
            return False
        else:
            logger.info("Response unclear")
            return None
    except Exception as e:
        logger.error(f"Error interpreting yes/no response: {e}")
        return None
