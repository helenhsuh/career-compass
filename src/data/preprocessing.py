"""
Preprocessing utilities for text normalization and feature extraction.
"""

import re

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text
