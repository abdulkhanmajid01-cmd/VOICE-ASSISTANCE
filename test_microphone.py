#!/usr/bin/env python3
"""
Microphone Debug Test Script
Tests if microphone is working properly
"""

import speech_recognition as sr
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_microphone():
    """Test microphone connectivity and functionality"""
    print("\n" + "="*60)
    print("MICROPHONE DEBUG TEST")
    print("="*60 + "\n")
    
    # Test 1: Check available microphones
    print("TEST 1: Available Microphones")
    print("-" * 60)
    try:
        mic_list = sr.Microphone.list_microphone_indexes()
        print(f"✓ Found microphones: {mic_list}")
        
        for i in mic_list:
            print(f"  Microphone {i}: {sr.Microphone.list_microphone_indexes()}")
    except Exception as e:
        print(f"✗ Error listing microphones: {e}")
        return False
    
    # Test 2: Initialize recognizer
    print("\nTEST 2: Initializer Recognizer")
    print("-" * 60)
    try:
        recognizer = sr.Recognizer()
        print(f"✓ Recognizer initialized")
        print(f"  Energy threshold: {recognizer.energy_threshold}")
        print(f"  Dynamic threshold: {recognizer.dynamic_energy_threshold}")
    except Exception as e:
        print(f"✗ Error initializing recognizer: {e}")
        return False
    
    # Test 3: Try to listen
    print("\nTEST 3: Listening Test (Wait 3 seconds and speak)")
    print("-" * 60)
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... (waiting 1 second)")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            print("✓ Microphone detected!")
            print(f"✓ Ambient noise adjusted")
            print("\nLISTENING... (Speak now!)")
            
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            print("✓ Audio captured!")
            
            # Try to recognize
            print("\nRecognizing audio...")
            text = recognizer.recognize_google(audio)
            print(f"✓ Recognized: '{text}'")
            return True
            
    except sr.WaitTimeoutError:
        print("✗ Timeout - No speech detected. Check microphone!")
        print("  Possible fixes:")
        print("  - Check microphone is connected")
        print("  - Speak louder")
        print("  - Reduce background noise")
        return False
    except sr.UnknownValueError:
        print("✗ Audio not understood. Try speaking more clearly.")
        return False
    except sr.RequestError as e:
        print(f"✗ Google API error: {e}")
        print("  Check internet connection!")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_microphone()
    
    print("\n" + "="*60)
    if success:
        print("✓ MICROPHONE TEST PASSED")
        print("\nYour microphone is working! Try running:")
        print("  python main.py --gui")
    else:
        print("✗ MICROPHONE TEST FAILED")
        print("\nTroubleshooting steps:")
        print("1. Check microphone is connected")
        print("2. Check Windows volume is ON")
        print("3. Test microphone in System Settings")
        print("4. Try: python -c \"import pyaudio; print('PyAudio OK')\"")
    print("="*60 + "\n")
