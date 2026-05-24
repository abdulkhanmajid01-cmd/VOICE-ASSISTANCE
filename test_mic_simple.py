#!/usr/bin/env python3
"""Simple Microphone Test"""

import speech_recognition as sr

print("\n" + "="*60)
print("SIMPLE MICROPHONE TEST")
print("="*60 + "\n")

try:
    print("1. Initializing recognizer...")
    recognizer = sr.Recognizer()
    print("   ✓ Success\n")
    
    print("2. Attempting to access microphone...")
    with sr.Microphone() as source:
        print("   ✓ Microphone found!\n")
        
        print("3. Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("   ✓ Success\n")
        
        print("4. LISTENING... (Speak now! - waiting 5 seconds)")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        print("   ✓ Audio captured\n")
        
        print("5. Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"   ✓ RECOGNIZED: '{text}'\n")
        
        print("="*60)
        print("✓ MICROPHONE WORKING!")
        print("="*60 + "\n")
        
except sr.WaitTimeoutError:
    print("   ✗ TIMEOUT - No speech detected\n")
    print("="*60)
    print("✗ Microphone not detecting speech!")
    print("="*60)
    print("\nPossible issues:")
    print("- Microphone not connected")
    print("- Microphone is disabled")
    print("- System volume is muted")
    print("- Need to speak louder")
    print("\n")
except sr.UnknownValueError:
    print("   ✗ Could not understand audio\n")
except sr.RequestError as e:
    print(f"   ✗ API Error: {e}\n")
except OSError as e:
    print(f"   ✗ Microphone Error: {e}\n")
    print("="*60)
    print("✗ MICROPHONE NOT FOUND!")
    print("="*60)
    print("\nYou need to:")
    print("1. Connect a microphone to your system")
    print("2. Or use interactive mode: python main.py --mode interactive\n")
except Exception as e:
    print(f"   ✗ Error: {e}\n")
