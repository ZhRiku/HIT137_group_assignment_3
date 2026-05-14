"""
HIT137 Assignment 3 - Spot the Difference Game
Author: Replace with your group members' names
Description:
    Desktop application using Tkinter and OpenCV.
    Loads an image, creates a modified clone with exactly 5 random non-overlapping
    differences, and lets the player find them by clicking the modified image.

Requirements covered:
    - OOP design with multiple classes
    - Tkinter GUI
    - OpenCV image processing
    - JPG, PNG, BMP loading
    - Side-by-side original and modified images
    - 5 non-overlapping randomized differences
    - At least 3 alteration types
    - Click detection, scoring, mistakes, lockout, and reveal feature
"""

import random
import tkinter as tk
from tkinter import filedialog, messagebox
from dataclasses import dataclass
from abc import ABC, abstractmethod

import cv2
import numpy as np
from PIL import Image, ImageTk


# ----------------------------- Data Classes -----------------------------




# -------------------------- Alteration Classes --------------------------




# ------------------------- Difference Generator -------------------------
 """Creates exactly five random, non-overlapping differences using OpenCV."""

   TOTAL_DIFFERENCES = 5

    def __init__(self):
        self.alterations = [
            ColourShiftAlteration(),
            BlurAlteration(),
            BrightnessAlteration(),
            SmallShapeAlteration(),
        ]

    def generate(self, original_image: np.ndarray):
        """Returns a modified image and a list of generated difference regions."""
        modified_image = original_image.copy()
        height, width = original_image.shape[:2]
        regions = []

        min_size = max(24, min(width, height) // 16)
        max_size = max(36, min(width, height)

        attempts = 0
        while len(regions) < self.TOTAL_DIFFERENCES and attempts < 1000:
            attempts += 1

            region_w = random.randint(min_size, max_size)
            region_h = random.randint(min_size, max_size)

            if width <= region_w + 20 or height <= region_h + 20:
                raise ValueError("Image is too small. Please choose a larger image.")

            x = random.randint(10, width - region_w - 10)
            y = random.randint(10, height - region_h - 10)

            alteration = random.choice(self.alterations)
            new_region = DifferenceRegion(x, y, region_w, region_h, alteration.name)

            if all(not new_region.overlaps(existing) for existing in regions):
                alteration.apply(modified_image, new_region)
                regions.append(new_region)

        if len(regions) != self.TOTAL_DIFFERENCES:
            raise ValueError("Could not create 5 non-overlapping differences. Try a larger image.")

        return modified_image, regions



# ----------------------------- GUI Class -----------------------------


