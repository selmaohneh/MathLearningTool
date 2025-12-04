# Math Learning Tool

An interactive desktop application to help children (ages 5-7) learn number decomposition for numbers 4-10. This tool provides three progressive levels of difficulty, replacing manual training sessions with an engaging, self-paced learning experience.

## Features

- **Three Learning Levels:**
  - **Level 1**: Visual split with divider - See all dots arranged horizontally with a visual divider, enter both numbers. Dots are grouped in fives for easy counting.
  - **Level 2**: Partial dots with pre-filled input - Only leftmost dots are shown (horizontally in groups of five), left input shows the visible count, child only enters the missing number
  - **Level 3**: Mental math - Pure calculation with pre-filled first number

- **Interactive UI:**
  - Simple, distraction-free design suitable for young children
  - Easy level and number selection (4-10)
  - Visual and audio feedback for correct/incorrect answers
  - Automatic progression through exercises

- **Cross-Platform:**
  - Runs on Windows and Linux
  - Built with Python and Tkinter (standard GUI library)

## Requirements

### All Platforms
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Optional (for audio feedback)
- pygame library
- numpy library (for sound generation)

## Quick Start

After installation, you can verify your setup:
```bash
python test_setup.py
```

This will check all dependencies and report any issues.

## Installation

### Windows

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"
   - Tkinter is included by default

2. **Install dependencies**:
   ```bash
   cd path\to\math
   pip install -r requirements.txt
   ```

3. **Generate sound files** (optional but recommended):
   ```bash
   python generate_sounds.py
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

### Linux (Ubuntu/Debian)

1. **Install Python and Tkinter**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-tk python3-pip
   ```

2. **Install dependencies**:
   ```bash
   cd /path/to/math
   pip3 install -r requirements.txt
   ```

3. **Generate sound files** (optional but recommended):
   ```bash
   python3 generate_sounds.py
   ```

4. **Run the application**:
   ```bash
   python3 app.py
   ```

   Or make it executable:
   ```bash
   chmod +x app.py
   ./app.py
   ```

### Linux (Fedora/RHEL)

```bash
sudo dnf install python3 python3-tkinter
pip3 install -r requirements.txt
python3 generate_sounds.py
python3 app.py
```

## Usage

### Basic Operation

1. **Start the application**: Run `python app.py` (or `python3 app.py` on Linux)

2. **Select a level**: Click buttons 1-3 in the left sidebar
   - Start with Level 1 for beginners
   - Progress to Level 2 when comfortable
   - Use Level 3 for mental math practice

3. **Select a number**: Click numbers 4-10 in the left sidebar
   - Start with smaller numbers (4-6) for beginners
   - Progress to larger numbers (7-10) as skills improve

4. **Answer the questions**:
   - **Level 1**: Type the first number, then the second number (auto-checks when both are entered)
   - **Level 2**: Type only the missing number (visible count is pre-filled in left box, auto-checks as you type)
   - **Level 3**: Type only the missing number (first is pre-filled, auto-checks as you type)

5. **Feedback**:
   - ✓ Green text + high beep = Correct! (auto-advances)
   - Red text + low beep = Try again (keeps same question)

### Teaching Tips

- **Session Length**: Keep sessions to 10 minutes or based on child's concentration
- **Progression**: Master each level before moving to the next
- **Number Selection**: Start with 4-5, gradually increase to 10
- **Encouragement**: Celebrate correct answers, stay patient with mistakes
- **Mix It Up**: Vary between levels and numbers to maintain interest

## Audio Setup

### Default Sounds

The application includes a sound generator that creates simple beep sounds:
- **Correct answer**: High-pitched beep (880 Hz)
- **Wrong answer**: Low-pitched beep (261 Hz)

Run `python generate_sounds.py` to create these sounds.

### Custom Sounds

You can replace the generated sounds with your own:

1. Find or create two WAV files (any sample rate, mono or stereo)
2. Name them:
   - `correct.wav` - played on correct answers
   - `wrong.wav` - played on incorrect answers
3. Place them in the `sounds/` directory
4. Restart the application

**Tips for custom sounds:**
- Keep sounds short (0.2-0.5 seconds)
- Use positive, encouraging sounds for correct answers
- Use gentle, neutral sounds for wrong answers (avoid negative sounds)
- Test volume levels - sounds should be noticeable but not startling

### Running Without Audio

The application works perfectly without audio if:
- pygame is not installed
- Sound files are missing
- You prefer silent operation

A warning message will appear in the terminal, but all functionality remains available.

## Troubleshooting

### Tkinter Not Found (Linux)

**Error**: `ModuleNotFoundError: No module named '_tkinter'`

**Solution**:
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora/RHEL
sudo dnf install python3-tkinter
```

### Pygame Not Installing

**Solution**: Try installing from system packages:
```bash
# Ubuntu/Debian
sudo apt install python3-pygame

# Fedora/RHEL
sudo dnf install python3-pygame
```

### No Sound

**Possible causes and solutions**:
1. pygame not installed: `pip install pygame`
2. Sound files missing: Run `python generate_sounds.py`
3. System volume muted: Check system audio settings
4. Audio driver issues: The app will still work, just without sound

### Window Too Small/Large

Edit `app.py` line 20 to adjust size:
```python
self.root.geometry("900x600")  # Change width x height
```

## Project Structure

```
math/
├── app.py                 # Main application entry point
├── audio_manager.py       # Audio playback system
├── levels/                # Level implementations
│   ├── __init__.py
│   ├── level1.py         # Visual split with divider
│   ├── level2.py         # Partial dots display
│   └── level3.py         # Mental math
├── sounds/                # Audio files directory
│   ├── correct.wav       # Correct answer sound
│   └── wrong.wav         # Wrong answer sound
├── generate_sounds.py    # Script to create sound files
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md
```

## Development

### Running in Development Mode

```bash
python app.py
```

### Testing Checklist

- [ ] All three levels load correctly
- [ ] Number selection (4-10) works in each level
- [ ] Level 1: All dots shown horizontally in groups of five with divider line, both inputs work, auto-checks when both entered
- [ ] Level 2: Only leftmost visible dots shown horizontally (hidden dots completely invisible), left input pre-filled with visible count (read-only), only right input needed, auto-checks as you type
- [ ] Level 3: Left number pre-filled, only right input needed, auto-checks as you type
- [ ] Correct answers trigger green feedback and sound
- [ ] Wrong answers trigger red feedback and sound
- [ ] Edge cases work (0+N, N+0)
- [ ] Rapid input doesn't cause issues
- [ ] Switching levels/numbers resets state correctly
- [ ] Exercises never repeat consecutively (each correct answer shows a different exercise)

### Customization

**Colors**: Edit the color codes in level files:
- `#4CAF50` - Green (correct)
- `#FF5722` - Red (wrong/divider)
- `#2196F3` - Blue (dots/buttons)

**Fonts**: Adjust font sizes in each level's `create_widgets()` method.

**Layout**: Modify `app.py` geometry and grid settings.

## Educational Background

This tool implements the "number bonds" or "part-part-whole" method for teaching early arithmetic:

1. **Decomposition**: Understanding that numbers can be split into parts
2. **Composition**: Recognizing that parts combine to make wholes
3. **Mental Flexibility**: Building multiple representations of the same number
4. **Foundation**: Essential for addition, subtraction, and number sense

The three levels provide scaffolded learning:
- **Concrete** (Level 1): Visual with physical representation
- **Pictorial** (Level 2): Visual with missing elements
- **Abstract** (Level 3): Mental calculation only

## License

This project is provided as-is for personal and educational use.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Verify Python and Tkinter are properly installed
3. Test with a simple Python Tkinter program
4. Check terminal output for error messages

## Version History

- **v1.3** (2025) - Level 2 enhancement
  - Level 2: Left input box now pre-filled with visible dots count (read-only)
  - Level 2: Player only needs to enter the missing number in right input box
  - Level 2: Simplified interaction - focus automatically set to right input
  - Enhanced learning progression with clearer scaffolding between levels

- **v1.2** (2025) - UX improvements
  - Auto-check feature: Level 1 & 2 now automatically check answers when both numbers are entered (no Enter key needed)
  - Level 2: Visible dots now always shown left-most for clearer pattern recognition
  - Anti-repetition: Exercises never repeat consecutively, ensuring varied practice
  - Improved learning flow with faster feedback

- **v1.1** (2025) - Visual improvements
  - All dots now displayed horizontally on a single line (improved readability)
  - Visual grouping: Small gap after 5th dot helps children recognize groups of five
  - Level 2: Hidden dots now completely invisible (removed grayed-out placeholders to encourage mental calculation)
  - Fixed cross-platform color compatibility issue

- **v1.0** (2025) - Initial release
  - Three levels of progressive difficulty
  - Numbers 4-10 support
  - Audio feedback with pygame
  - Cross-platform Windows/Linux support
