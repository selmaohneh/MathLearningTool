"""
Level 1: Visual Split with Divider
Shows dots with a vertical divider line, child enters both numbers
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


class Level1(tk.Frame):
    def __init__(self, parent, number):
        super().__init__(parent, bg="white")
        self.number = number
        self.divider_position = 0

        # Create UI elements
        self.create_widgets()
        self.randomize_divider()

    def create_widgets(self):
        """Create all UI components for Level 1"""
        # Number display at top
        self.number_label = tk.Label(
            self,
            text=str(self.number),
            font=("Arial", 48, "bold"),
            bg="white",
            fg="#333"
        )
        self.number_label.pack(pady=(20, 10))

        # Canvas for dots and divider
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

        # Left input box
        self.left_entry = tk.Entry(
            input_frame,
            width=5,
            font=("Arial", 36),
            justify="center",
            bd=2,
            relief="solid"
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

        # Bind keyboard events
        self.left_entry.bind("<KeyRelease>", self.on_key_release)
        self.right_entry.bind("<KeyRelease>", self.on_key_release)
        self.left_entry.bind("<Return>", self.check_answer)
        self.right_entry.bind("<Return>", self.check_answer)

        # Set focus to left entry
        self.left_entry.focus_set()

        # Feedback label (hidden initially)
        self.feedback_label = tk.Label(
            self,
            text="",
            font=("Arial", 24),
            bg="white"
        )
        self.feedback_label.pack(pady=10)

    def draw_dots(self):
        """Draw dots on canvas with divider line"""
        self.canvas.delete("all")

        # Calculate dot layout
        dots_per_row = min(5, self.number)
        rows = math.ceil(self.number / dots_per_row)

        dot_radius = 20
        spacing_x = 80
        spacing_y = 80

        # Center the dots
        total_width = dots_per_row * spacing_x
        total_height = rows * spacing_y
        start_x = (600 - total_width) / 2 + spacing_x / 2
        start_y = (250 - total_height) / 2 + spacing_y / 2

        # Draw dots
        dot_positions = []
        for i in range(self.number):
            row = i // dots_per_row
            col = i % dots_per_row
            x = start_x + col * spacing_x
            y = start_y + row * spacing_y

            # Determine if dot is on left or right of divider
            color = "#4CAF50" if i < self.divider_position else "#2196F3"

            self.canvas.create_oval(
                x - dot_radius, y - dot_radius,
                x + dot_radius, y + dot_radius,
                fill=color,
                outline="#333",
                width=2
            )
            dot_positions.append((x, y))

        # Draw divider line between dots
        if 0 < self.divider_position < self.number:
            # Find the divider position
            left_idx = self.divider_position - 1
            right_idx = self.divider_position

            left_row = left_idx // dots_per_row
            left_col = left_idx % dots_per_row
            right_row = right_idx // dots_per_row
            right_col = right_idx % dots_per_row

            # Draw vertical divider
            if left_row == right_row:
                # Same row - draw vertical line between them
                left_x = start_x + left_col * spacing_x
                right_x = start_x + right_col * spacing_x
                divider_x = (left_x + right_x) / 2
                y = start_y + left_row * spacing_y

                self.canvas.create_line(
                    divider_x, y - 40,
                    divider_x, y + 40,
                    fill="#FF5722",
                    width=4
                )
            else:
                # Different rows - draw line at end of first row
                divider_x = start_x + (dots_per_row - 0.5) * spacing_x
                y1 = start_y + left_row * spacing_y
                y2 = start_y + right_row * spacing_y

                self.canvas.create_line(
                    divider_x, y1 - 40,
                    divider_x, (y1 + y2) / 2,
                    fill="#FF5722",
                    width=4
                )

    def randomize_divider(self):
        """Randomly place the divider between dots"""
        # Divider can be at positions 1 to number-1 (not at 0 or number)
        self.divider_position = random.randint(1, self.number - 1)
        self.draw_dots()

    def on_key_release(self, event):
        """Handle keyboard input to move between boxes"""
        widget = event.widget
        content = widget.get()

        # Only allow digits
        if content and not content.isdigit():
            widget.delete(0, tk.END)
            return

        # If left box has content and we're in left box, move to right box
        if widget == self.left_entry and content:
            if len(content) > 2:  # Limit to 2 digits
                widget.delete(2, tk.END)
            self.right_entry.focus_set()

    def check_answer(self, event=None):
        """Check if the answer is correct"""
        try:
            left_val = int(self.left_entry.get()) if self.left_entry.get() else None
            right_val = int(self.right_entry.get()) if self.right_entry.get() else None

            if left_val is None or right_val is None:
                return

            # Check if answer is correct
            if left_val + right_val == self.number and left_val == self.divider_position:
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
        self.randomize_divider()
        self.left_entry.focus_set()

    def on_wrong(self):
        """Handle wrong answer"""
        self.feedback_label.config(text="")
        self.clear_inputs()
        self.left_entry.focus_set()

    def clear_inputs(self):
        """Clear both input boxes"""
        self.left_entry.delete(0, tk.END)
        self.right_entry.delete(0, tk.END)

    def set_number(self, number):
        """Update the number being practiced"""
        self.number = number
        self.number_label.config(text=str(number))
        self.clear_inputs()
        self.randomize_divider()
        self.left_entry.focus_set()
