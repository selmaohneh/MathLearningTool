#!/usr/bin/env python3
"""
Test script to verify the Math Learning Tool setup
Run this to check if all dependencies are properly installed
"""

import sys


def test_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("  ⚠ Warning: Python 3.7+ recommended")
        return False
    return True


def test_tkinter():
    """Check if Tkinter is available"""
    try:
        import tkinter
        print("✓ Tkinter available")
        return True
    except ImportError:
        print("✗ Tkinter NOT available")
        print("  Install with:")
        print("    Ubuntu/Debian: sudo apt install python3-tk")
        print("    Fedora/RHEL: sudo dnf install python3-tkinter")
        return False


def test_pygame():
    """Check if pygame is available (optional)"""
    try:
        import pygame
        print(f"✓ pygame {pygame.version.ver} available")
        return True
    except ImportError:
        print("⚠ pygame NOT available (optional)")
        print("  Audio feedback will not work")
        print("  Install with: pip install pygame")
        return False


def test_numpy():
    """Check if numpy is available (optional)"""
    try:
        import numpy
        print(f"✓ numpy {numpy.__version__} available")
        return True
    except ImportError:
        print("⚠ numpy NOT available (optional)")
        print("  Only needed for sound generation")
        return False


def test_sound_files():
    """Check if sound files exist"""
    import os
    sounds_dir = os.path.join(os.path.dirname(__file__), 'sounds')
    correct_wav = os.path.join(sounds_dir, 'correct.wav')
    wrong_wav = os.path.join(sounds_dir, 'wrong.wav')

    correct_exists = os.path.exists(correct_wav)
    wrong_exists = os.path.exists(wrong_wav)

    if correct_exists and wrong_exists:
        print("✓ Sound files present")
        return True
    else:
        print("⚠ Sound files missing")
        if not correct_exists:
            print(f"  Missing: {correct_wav}")
        if not wrong_exists:
            print(f"  Missing: {wrong_wav}")
        print("  Run: python generate_sounds.py")
        return False


def test_imports():
    """Test if application modules can be imported"""
    try:
        import app
        print("✓ Main application module loads")
        return True
    except ImportError as e:
        print(f"✗ Failed to load application: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 50)
    print("Math Learning Tool - Setup Verification")
    print("=" * 50)
    print()

    results = []

    print("[1/6] Checking Python version...")
    results.append(test_python_version())
    print()

    print("[2/6] Checking Tkinter (required)...")
    results.append(test_tkinter())
    print()

    print("[3/6] Checking pygame (optional)...")
    results.append(test_pygame())
    print()

    print("[4/6] Checking numpy (optional)...")
    results.append(test_numpy())
    print()

    print("[5/6] Checking sound files...")
    results.append(test_sound_files())
    print()

    print("[6/6] Checking application modules...")
    results.append(test_imports())
    print()

    print("=" * 50)
    if results[0] and results[1]:  # Python and Tkinter are required
        print("✓ Setup complete! Ready to run: python app.py")
        if not all(results[2:]):
            print("  (Some optional features unavailable)")
    else:
        print("✗ Setup incomplete - fix required items above")
    print("=" * 50)


if __name__ == "__main__":
    main()
