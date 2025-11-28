#!/usr/bin/env python3
"""
Math Learning Tool - Interactive number decomposition trainer for children
"""

import tkinter as tk
from tkinter import font as tkfont
import sys
import os

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3


class MathLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Learning Tool")
        self.root.geometry("900x600")
        self.root.configure(bg="#F0F0F0")

        # Configure grid weights for responsive layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # State
        self.current_level = 1
        self.current_number = 5
        self.current_level_widget = None

        # Create UI components
        self.create_sidebar()
        self.create_main_panel()

        # Load initial level
        self.load_level(self.current_level)

    def create_sidebar(self):
        """Create left sidebar with level and number selectors"""
        sidebar = tk.Frame(self.root, bg="#E0E0E0", width=150, padx=10, pady=20)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        # Level selector section
        level_label = tk.Label(
            sidebar,
            text="Level",
            bg="#E0E0E0",
            font=("Arial", 14, "bold")
        )
        level_label.pack(pady=(0, 10))

        self.level_buttons = {}
        for level in range(1, 4):
            btn = tk.Button(
                sidebar,
                text=str(level),
                width=8,
                height=2,
                font=("Arial", 12),
                command=lambda l=level: self.select_level(l)
            )
            btn.pack(pady=5)
            self.level_buttons[level] = btn

        # Separator
        separator = tk.Frame(sidebar, bg="#A0A0A0", height=2)
        separator.pack(pady=20, fill="x")

        # Number selector section
        number_label = tk.Label(
            sidebar,
            text="Number",
            bg="#E0E0E0",
            font=("Arial", 14, "bold")
        )
        number_label.pack(pady=(0, 10))

        self.number_buttons = {}
        for num in range(4, 11):
            btn = tk.Button(
                sidebar,
                text=str(num),
                width=8,
                height=1,
                font=("Arial", 11),
                command=lambda n=num: self.select_number(n)
            )
            btn.pack(pady=3)
            self.number_buttons[num] = btn

        # Highlight initial selections
        self.update_button_highlights()

    def create_main_panel(self):
        """Create main panel for level display"""
        self.main_panel = tk.Frame(self.root, bg="white")
        self.main_panel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.main_panel.grid_rowconfigure(0, weight=1)
        self.main_panel.grid_columnconfigure(0, weight=1)

    def select_level(self, level):
        """Handle level selection"""
        if self.current_level != level:
            self.current_level = level
            self.update_button_highlights()
            self.load_level(level)

    def select_number(self, number):
        """Handle number selection"""
        if self.current_number != number:
            self.current_number = number
            self.update_button_highlights()
            if self.current_level_widget:
                self.current_level_widget.set_number(number)

    def update_button_highlights(self):
        """Update button colors to show current selection"""
        # Update level buttons
        for level, btn in self.level_buttons.items():
            if level == self.current_level:
                btn.config(bg="#4CAF50", fg="white", relief="sunken")
            else:
                btn.config(bg="SystemButtonFace", fg="black", relief="raised")

        # Update number buttons
        for num, btn in self.number_buttons.items():
            if num == self.current_number:
                btn.config(bg="#2196F3", fg="white", relief="sunken")
            else:
                btn.config(bg="SystemButtonFace", fg="black", relief="raised")

    def load_level(self, level):
        """Load the specified level into the main panel"""
        # Clear existing level widget
        if self.current_level_widget:
            self.current_level_widget.destroy()

        # Create new level widget
        if level == 1:
            self.current_level_widget = Level1(self.main_panel, self.current_number)
        elif level == 2:
            self.current_level_widget = Level2(self.main_panel, self.current_number)
        elif level == 3:
            self.current_level_widget = Level3(self.main_panel, self.current_number)

        if self.current_level_widget:
            self.current_level_widget.pack(fill="both", expand=True)


def main():
    root = tk.Tk()
    app = MathLearningApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
