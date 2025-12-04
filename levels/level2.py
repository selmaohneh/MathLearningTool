"""
Level 2: Partial Dots Display
Shows only some dots arranged horizontally (grouped in fives with gap after 5th dot).
Hidden dots are completely invisible - not shown at all.
Child must calculate the missing portion mentally.
"""

import tkinter as tk
from tkinter import Canvas
import random
import math
import sys
import os

# Import audio manager
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from audio_manager import get_audio_manager


class Level2(tk.Frame):
    def __init__(self, parent, number):
        super().__init__(parent, bg="white")
        self.number = number
        self.visible_dots = 0
        self.hidden_dots = 0

        # Create UI elements
        self.create_widgets()
        self.randomize_dots()

    def create_widgets(self):
        """Create all UI components for Level 2"""
        # Number display at top
        self.number_label = tk.Label(
            self,
            text=str(self.number),
            font=("Arial", 48, "bold"),
            bg="white",
            fg="#333"
        )
        self.number_label.pack(pady=(20, 10))

        # Canvas for dots
        self.canvas = Canvas(
            self,
            width=600,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack(pady=20)

        # Input frame
        input_frame = tk.Frame(self, bg="white")
        input_frame.pack(pady=20)

        # Left input box (pre-filled with visible dots count)
        self.left_entry = tk.Entry(
            input_frame,
            width=5,
            font=("Arial", 36),
            justify="center",
            bd=2,
            relief="solid",
            state="readonly",
            readonlybackground="white",
            fg="#333"
        )
        self.left_entry.pack(side="left", padx=10)

        # Plus sign
        plus_label = tk.Label(
            input_frame,
            text="+",
            font=("Arial", 36),
            bg="white"
        )
        plus_label.pack(side="left", padx=10)

        # Right input box
        self.right_entry = tk.Entry(
            input_frame,
            width=5,
            font=("Arial", 36),
            justify="center",
            bd=2,
            relief="solid"
        )
        self.right_entry.pack(side="left", padx=10)

        # Bind keyboard events (only for right entry)
        self.right_entry.bind("<KeyRelease>", self.on_key_release)
        self.right_entry.bind("<Return>", self.check_answer)

        # Set focus to right entry since left is pre-filled
        self.right_entry.focus_set()

        # Feedback label (hidden initially)
        self.feedback_label = tk.Label(
            self,
            text="",
            font=("Arial", 24),
            bg="white"
        )
        self.feedback_label.pack(pady=10)

    def draw_dots(self):
        """Draw only visible dots horizontally with grouping by fives (hidden dots not drawn)"""
        self.canvas.delete("all")

        dot_radius = 20
        spacing_x = 50  # Regular spacing between dots
        gap_after_five = 30  # Extra gap after 5th dot

        # Calculate total width including the gap
        total_width = (self.number * spacing_x) + (gap_after_five if self.number > 5 else 0)
        start_x = (600 - total_width) / 2 + spacing_x / 2
        y = 125  # Center vertically

        # Show only the leftmost visible dots
        visible_indices = set(range(self.visible_dots))

        # Draw only visible dots horizontally
        for i in range(self.number):
            if i in visible_indices:
                # Add extra gap after the 5th dot
                x_offset = gap_after_five if i >= 5 else 0
                x = start_x + (i * spacing_x) + x_offset

                # Draw visible dot
                self.canvas.create_oval(
                    x - dot_radius, y - dot_radius,
                    x + dot_radius, y + dot_radius,
                    fill="#4CAF50",
                    outline="#333",
                    width=2
                )

    def randomize_dots(self):
        """Randomly decide how many dots are visible vs hidden, ensuring different from previous"""
        # Show between 1 and (number-1) dots
        # This ensures there's always something hidden and something visible
        if self.number > 2:
            # If there are multiple possible values, ensure we get a different one
            new_visible = self.visible_dots
            while new_visible == self.visible_dots:
                new_visible = random.randint(1, self.number - 1)
            self.visible_dots = new_visible
        elif self.number == 2:
            # For number=2, toggle between 1 and 1 (only one option, so it will repeat)
            # Actually for 2, we can only show 1 dot, so we can't avoid repetition
            self.visible_dots = 1
        else:
            self.visible_dots = 1

        self.hidden_dots = self.number - self.visible_dots
        self.draw_dots()

        # Pre-fill the left entry with the visible dots count
        self.update_left_entry()

    def update_left_entry(self):
        """Update the left entry with the visible dots count"""
        # Temporarily enable the entry to update its value
        self.left_entry.config(state="normal")
        self.left_entry.delete(0, tk.END)
        self.left_entry.insert(0, str(self.visible_dots))
        self.left_entry.config(state="readonly")

    def on_key_release(self, event):
        """Handle keyboard input and auto-check"""
        widget = event.widget
        content = widget.get()

        # Only allow digits
        if content and not content.isdigit():
            widget.delete(0, tk.END)
            return

        # Limit to 2 digits
        if len(content) > 2:
            widget.delete(2, tk.END)

        # Auto-check when right box has a value (left is pre-filled)
        if self.right_entry.get():
            self.check_answer()

    def check_answer(self, event=None):
        """Check if the answer is correct"""
        try:
            right_val = int(self.right_entry.get()) if self.right_entry.get() else None

            if right_val is None:
                return

            # Check if the answer is correct (left is pre-filled with visible_dots)
            if right_val == self.hidden_dots:
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
        """Handle correct answer"""
        self.feedback_label.config(text="")
        self.clear_inputs()
        self.randomize_dots()
        self.right_entry.focus_set()

    def on_wrong(self):
        """Handle wrong answer"""
        self.feedback_label.config(text="")
        self.clear_inputs()
        self.right_entry.focus_set()

    def clear_inputs(self):
        """Clear only the right input box (left is pre-filled)"""
        self.right_entry.delete(0, tk.END)

    def set_number(self, number):
        """Update the number being practiced"""
        self.number = number
        self.number_label.config(text=str(number))
        self.clear_inputs()
        self.randomize_dots()
        self.right_entry.focus_set()
