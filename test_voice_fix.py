#!/usr/bin/env python3
"""
Test script to verify voice response fix
Tests multiple commands to ensure TTS works consistently
"""

import sys
import time
from core.speech_engine import get_speech_engine

def test_voice_responses():
    """Test multiple voice responses in sequence"""
    print("=" * 60)
    print("VOICE RESPONSE TEST")
    print("=" * 60)
    print()
    
    try:
        speech_engine = get_speech_engine()
        
        # Test commands
        test_messages = [
            "Opening YouTube",
            "Opening Google",
            "Opening GitHub",
            "The current time is 3 o'clock",
            "Playing Believer on YouTube",
            "It's Monday May 18th 2026",
            "Voice response test complete",
        ]
        
        print(f"Testing {len(test_messages)} voice responses...\n")
        
        for i, message in enumerate(test_messages, 1):
            print(f"[{i}] Speaking: {message}")
            speech_engine.speak(message)
            # Give TTS time to complete (adjust as needed)
            time.sleep(2)
        
        print("\n" + "=" * 60)
        print("TEST COMPLETED SUCCESSFULLY!")
        print("All voice responses should have played without stopping.")
        print("=" * 60)
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = test_voice_responses()
    sys.exit(0 if success else 1)
