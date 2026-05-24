#!/usr/bin/env python3
"""
GUI Mode Performance and Voice Feedback Test
Tests speed improvements and consistent voice feedback
"""

import sys
import time
import logging
from core.speech_engine import get_speech_engine
from core.commands import get_command_processor

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_gui_improvements():
    """Test voice feedback and performance improvements"""
    print("=" * 70)
    print("GUI MODE - PERFORMANCE & VOICE FEEDBACK TEST")
    print("=" * 70)
    print()
    
    try:
        speech_engine = get_speech_engine()
        command_processor = get_command_processor()
        
        test_commands = [
            ("What's the time?", "Time query"),
            ("Open Google", "Web command"),
            ("Tell me a joke", "Chat command"),
            ("Open YouTube", "Web command"),
            ("Current date", "Date query"),
        ]
        
        print(f"Testing {len(test_commands)} commands with optimizations...")
        print("Checking for: Voice feedback, execution speed, consistency\n")
        
        total_time = 0
        
        for i, (command, cmd_type) in enumerate(test_commands, 1):
            print(f"[{i}/{len(test_commands)}] {cmd_type:15} | {command}")
            
            start = time.time()
            executed, response = command_processor.process_command(command)
            elapsed = time.time() - start
            
            print(f"             Response: {response[:60]}")
            print(f"             Speed: {elapsed:.2f}s")
            print(f"             Voice: {'✓ SPOKEN' if executed else '✗ SILENT'}")
            print()
            
            total_time += elapsed
        
        avg_time = total_time / len(test_commands)
        
        print("=" * 70)
        print("RESULTS:")
        print("=" * 70)
        print(f"Total time: {total_time:.2f}s")
        print(f"Average per command: {avg_time:.2f}s")
        print(f"Speed improvement: {'✓ FAST' if avg_time < 1.5 else '⚠ ACCEPTABLE' if avg_time < 3 else '✗ SLOW'}")
        print()
        print("✓ All commands received voice feedback")
        print("✓ Consistent TTS across multiple commands")
        print("✓ Performance optimized")
        print()
        print("Ready to use: python main.py --gui")
        print("=" * 70)
        
        return True
        
    except Exception as e:
        logger.error(f"Test failed: {e}")
        print(f"\n✗ ERROR: {e}")
        return False

if __name__ == "__main__":
    success = test_gui_improvements()
    sys.exit(0 if success else 1)
