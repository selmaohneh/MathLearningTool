# Getting Started - Math Learning Tool

## For Immediate Use

### Windows
```bash
# 1. Open Command Prompt or PowerShell in the math directory
cd path\to\math

# 2. Install dependencies
pip install pygame

# 3. Verify setup (optional)
python test_setup.py

# 4. Run the application
python app.py
```

### Linux (Ubuntu/Debian)
```bash
# 1. Open terminal in the math directory
cd /path/to/math

# 2. Install Tkinter (if not already installed)
sudo apt install python3-tk

# 3. Install audio library
pip3 install pygame

# 4. Verify setup (optional)
python3 test_setup.py

# 5. Run the application
python3 app.py
```

## First Session with Your Daughter

1. **Start with Level 1, Number 4:**
   - Click "1" in the Level section
   - Click "4" in the Number section
   - Dots are shown horizontally with a red divider line between them
   - Help her understand: count the green dots (left side), count the blue dots (right side)
   - Type the numbers in both boxes (answer checks automatically when both are entered)
   - Note: Larger numbers show a gap after the 5th dot to help visualize groups of five

2. **Practice Pattern:**
   - 5-10 correct answers on number 4
   - Move to number 5
   - Continue through numbers 6-10 as comfortable

3. **Progress to Level 2:**
   - Once confident with Level 1
   - Same number range (4-10)
   - Now only leftmost dots are shown (some are completely hidden)
   - Child must calculate how many are missing
   - Answer checks automatically when both numbers are entered

4. **Advance to Level 3:**
   - Pure mental math
   - First number is shown, child calculates the second
   - Most challenging level

## Quick Tips

- **Session length:** 10 minutes or when focus drops
- **Best time:** When child is alert (after breakfast, not before bed)
- **Encouragement:** Celebrate correct answers enthusiastically
- **Mistakes:** Stay patient, say "try again" calmly
- **Variety:** Mix levels and numbers to keep interest
- **Daily practice:** 5-10 minutes daily is better than longer sessions less frequently

## Keyboard Shortcuts

- **Numbers 0-9:** Enter values
- **Automatic checking:**
  - Level 1 & 2: Checks when both numbers are entered
  - Level 3: Checks as you type
- **Enter:** Also submits answer (but not required)
- **Tab:** Move between input boxes (Level 1 & 2)

## Sound Notes

- High beep = Correct! ✓
- Low beep = Try again
- If no sound: App still works perfectly, sound is optional

## Troubleshooting First Run

### "ModuleNotFoundError: No module named '_tkinter'"
**Linux:** `sudo apt install python3-tk`

### "No module named 'pygame'" (and no sound)
**Any platform:** `pip install pygame`

### Sound files missing
**Run:** `python generate_sounds.py`

### Application won't start
**Run:** `python test_setup.py` to diagnose

## Customization

### Change Sound Files
Replace `sounds/correct.wav` and `sounds/wrong.wav` with your own WAV files (keep the names the same).

### Adjust Window Size
Edit `app.py` line 20:
```python
self.root.geometry("900x600")  # width x height in pixels
```

## Support Your Child's Learning

### Signs of Readiness to Progress

**Level 1 → Level 2:**
- Quickly answers 5+ correctly in a row
- Can do numbers 4-10 without hesitation
- Understands the concept (not just memorizing)

**Level 2 → Level 3:**
- Confidently calculates hidden dots
- Can explain their thinking
- Doesn't need to count on fingers

**To Next Number:**
- Completes current number quickly and accurately
- Shows confidence, not frustration

### What to Watch For

**Signs of struggle:**
- Takes >10 seconds to answer
- Multiple wrong attempts
- Shows frustration

**Response:** Drop back to easier level/number, no pressure!

**Signs of boredom:**
- Rushing through without thinking
- Losing focus

**Response:** Move up to harder level/number for challenge!

## Learning Outcomes

After regular practice, your daughter should:

1. **Instantly recall** number combinations (e.g., "7 is 4 and 3")
2. **Flexibly think** about numbers in multiple ways
3. **Quickly compute** simple addition/subtraction mentally
4. **Build confidence** with numbers and math

This foundation is crucial for:
- Addition facts (4+3=7)
- Subtraction facts (7-3=4)
- Place value understanding (teen numbers)
- Mental math strategies

## Questions?

See the main `README.md` for complete documentation.

Enjoy learning together! 📚✨
