"""
Level 3: Pure Mental Math
Shows only the number with pre-filled left value, child calculates the right value
"""

import tkinter as tk
import random
import sys
import os

# Import audio manager
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from audio_manager import get_audio_manager


class Level3(tk.Frame):
    def __init__(self, parent, number):
        super().__init__(parent, bg="white")
        self.number = number
        self.left_value = 0

        # Create UI elements
        self.create_widgets()
        self.generate_exercise()

    def create_widgets(self):
        """Create all UI components for Level 3"""
        # Number display at top
        self.number_label = tk.Label(
            self,
            text=str(self.number),
            font=("Arial", 64, "bold"),
            bg="white",
            fg="#333"
        )
        self.number_label.pack(pady=(60, 40))

        # Instruction text
        instruction_label = tk.Label(
            self,
            text="Split into:",
            font=("Arial", 20),
            bg="white",
            fg="#666"
        )
        instruction_label.pack(pady=(0, 30))

        # Input frame
        input_frame = tk.Frame(self, bg="white")
        input_frame.pack(pady=20)

        # Left input box (pre-filled, read-only)
        self.left_entry = tk.Entry(
            input_frame,
            width=5,
            font=("Arial", 48),
            justify="center",
            bd=2,
            relief="solid",
            state="readonly",
            readonlybackground="#E8F5E9",
            fg="#333"
        )
        self.left_entry.pack(side="left", padx=10)

        # Plus sign
        plus_label = tk.Label(
            input_frame,
            text="+",
            font=("Arial", 48),
            bg="white"
        )
        plus_label.pack(side="left", padx=10)

        # Right input box (user input)
        self.right_entry = tk.Entry(
            input_frame,
            width=5,
            font=("Arial", 48),
            justify="center",
            bd=2,
            relief="solid"
        )
        self.right_entry.pack(side="left", padx=10)

        # Bind keyboard events
        self.right_entry.bind("<KeyRelease>", self.on_key_release)
        self.right_entry.bind("<Return>", self.check_answer)

        # Set focus to right entry
        self.right_entry.focus_set()

        # Feedback label (hidden initially)
        self.feedback_label = tk.Label(
            self,
            text="",
            font=("Arial", 24),
            bg="white"
        )
        self.feedback_label.pack(pady=20)

    def generate_exercise(self):
        """Generate a new exercise with random left value, ensuring it's different from previous"""
        # Random value from 0 to number, but different from previous
        if self.number > 0:
            # If there are multiple possible values, ensure we get a different one
            new_value = self.left_value
            while new_value == self.left_value:
                new_value = random.randint(0, self.number)
            self.left_value = new_value
        else:
            # For number=0, there's only one option
            self.left_value = 0

        # Update left entry
        self.left_entry.config(state="normal")
        self.left_entry.delete(0, tk.END)
        self.left_entry.insert(0, str(self.left_value))
        self.left_entry.config(state="readonly")

        # Clear right entry
        self.right_entry.delete(0, tk.END)
        self.right_entry.focus_set()

    def on_key_release(self, event):
        """Handle keyboard input"""
        content = self.right_entry.get()

        # Only allow digits
        if content and not content.isdigit():
            self.right_entry.delete(0, tk.END)
            return

        # Limit to 2 digits
        if len(content) > 2:
            self.right_entry.delete(2, tk.END)
            return

        # Auto-check when user enters a value
        if content:
            self.check_answer()

    def check_answer(self, event=None):
        """Check if the answer is correct"""
        try:
            right_val = int(self.right_entry.get()) if self.right_entry.get() else None

            if right_val is None:
                return

            expected_value = self.number - self.left_value

            # Check if answer is correct
            if right_val == expected_value:
                self.show_feedback("Correct! ✓", "#4CAF50")
                get_audio_manager().play_correct()
                self.after(500, self.on_correct)
            else:
                self.show_feedback("Try again", "#FF5722")
                get_audio_manager().play_wrong()
                self.after(500, self.on_wrong)

        except ValueError:
            pass

    def show_feedback(self, message, color):
        """Display feedback message"""
        self.feedback_label.config(text=message, fg=color)

    def on_correct(self):
        """Handle correct answer - generate new exercise"""
        self.feedback_label.config(text="")
        self.generate_exercise()

    def on_wrong(self):
        """Handle wrong answer - clear right box only"""
        self.feedback_label.config(text="")
        self.right_entry.delete(0, tk.END)
        self.right_entry.focus_set()

    def set_number(self, number):
        """Update the number being practiced"""
        self.number = number
        self.number_label.config(text=str(number))
        self.generate_exercise()
