"""
Audio manager for playing sound effects
"""

import os
import sys

# Try to import pygame for audio, but don't fail if not available
try:
    import pygame
    pygame.mixer.init()
    AUDIO_AVAILABLE = True
except (ImportError, pygame.error):
    AUDIO_AVAILABLE = False
    print("Warning: Audio not available. Install pygame for sound effects: pip install pygame")


class AudioManager:
    """Manages audio playback for the application"""

    def __init__(self):
        self.sounds_dir = os.path.join(os.path.dirname(__file__), "sounds")
        self.sounds = {}
        self.enabled = AUDIO_AVAILABLE

        if self.enabled:
            self.load_sounds()

    def load_sounds(self):
        """Load sound files from the sounds directory"""
        sound_files = {
            'correct': 'correct.wav',
            'wrong': 'wrong.wav'
        }

        for key, filename in sound_files.items():
            filepath = os.path.join(self.sounds_dir, filename)
            if os.path.exists(filepath):
                try:
                    self.sounds[key] = pygame.mixer.Sound(filepath)
                except pygame.error as e:
                    print(f"Warning: Could not load {filename}: {e}")
            else:
                # Create a simple beep sound programmatically
                self.sounds[key] = self.create_beep(key)

    def create_beep(self, sound_type):
        """Create a simple beep sound programmatically"""
        try:
            # Create a simple sine wave beep
            import numpy as np

            sample_rate = 22050
            duration = 0.2  # seconds

            if sound_type == 'correct':
                # Higher pitch for correct (A5 = 880 Hz)
                frequency = 880
            else:
                # Lower pitch for wrong (C4 = 261 Hz)
                frequency = 261

            # Generate sine wave
            samples = np.sin(2 * np.pi * frequency * np.linspace(0, duration, int(sample_rate * duration)))

            # Apply envelope to avoid clicks
            envelope = np.concatenate([
                np.linspace(0, 1, int(sample_rate * 0.01)),  # Attack
                np.ones(int(sample_rate * (duration - 0.02))),  # Sustain
                np.linspace(1, 0, int(sample_rate * 0.01))  # Release
            ])

            samples = samples[:len(envelope)] * envelope

            # Convert to 16-bit integer
            samples = (samples * 32767).astype(np.int16)

            # Create stereo sound
            stereo_samples = np.column_stack((samples, samples))

            # Create pygame sound
            sound = pygame.sndarray.make_sound(stereo_samples)
            return sound

        except (ImportError, AttributeError):
            # If numpy is not available, return None
            return None

    def play(self, sound_name):
        """Play a sound effect"""
        if self.enabled and sound_name in self.sounds and self.sounds[sound_name]:
            try:
                self.sounds[sound_name].play()
            except pygame.error:
                pass  # Silently fail if audio playback fails

    def play_correct(self):
        """Play the correct answer sound"""
        self.play('correct')

    def play_wrong(self):
        """Play the wrong answer sound"""
        self.play('wrong')


# Global audio manager instance
_audio_manager = None


def get_audio_manager():
    """Get the global audio manager instance"""
    global _audio_manager
    if _audio_manager is None:
        _audio_manager = AudioManager()
    return _audio_manager
