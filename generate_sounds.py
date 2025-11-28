#!/usr/bin/env python3
"""
Generate simple WAV sound files for the math learning tool
Run this script to create correct.wav and wrong.wav in the sounds/ directory
"""

import os
import wave
import math
import struct


def generate_beep(filename, frequency, duration=0.3, sample_rate=22050):
    """Generate a simple beep sound and save as WAV file"""
    num_samples = int(sample_rate * duration)

    with wave.open(filename, 'w') as wav_file:
        # Set WAV file parameters
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 2 bytes per sample (16-bit)
        wav_file.setframerate(sample_rate)

        # Generate sine wave samples with envelope
        for i in range(num_samples):
            # Calculate sine wave value
            t = i / sample_rate
            value = math.sin(2 * math.pi * frequency * t)

            # Apply envelope to avoid clicks
            if i < sample_rate * 0.01:  # Attack
                envelope = i / (sample_rate * 0.01)
            elif i > num_samples - sample_rate * 0.01:  # Release
                envelope = (num_samples - i) / (sample_rate * 0.01)
            else:  # Sustain
                envelope = 1.0

            value *= envelope

            # Convert to 16-bit integer
            sample = int(value * 32767)
            wav_file.writeframes(struct.pack('<h', sample))

    print(f"Generated: {filename}")


def main():
    """Generate sound files"""
    # Create sounds directory if it doesn't exist
    sounds_dir = os.path.join(os.path.dirname(__file__), 'sounds')
    os.makedirs(sounds_dir, exist_ok=True)

    # Generate correct sound (higher pitch - A5 = 880 Hz)
    correct_file = os.path.join(sounds_dir, 'correct.wav')
    generate_beep(correct_file, frequency=880, duration=0.25)

    # Generate wrong sound (lower pitch - C4 = 261 Hz)
    wrong_file = os.path.join(sounds_dir, 'wrong.wav')
    generate_beep(wrong_file, frequency=261, duration=0.3)

    print("\nSound files created successfully!")
    print(f"Location: {sounds_dir}")


if __name__ == "__main__":
    main()
