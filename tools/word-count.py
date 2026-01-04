#!/usr/bin/env python3
"""
Word Count Tool for Patent Documents
Counts words in markdown files and checks against patent requirements.
"""

import sys
import re
from pathlib import Path


def count_words(text):
    """Count words in text, excluding markdown formatting."""
    # Remove markdown headers
    text = re.sub(r'#+\s+', '', text)
    # Remove markdown links but keep the text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove markdown bold/italic
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    # Remove code blocks
    text = re.sub(r'```[^`]*```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)
    # Split on whitespace and count
    words = text.split()
    return len(words)


def analyze_patent_document(file_path):
    """Analyze a patent document and provide word count analysis."""
    path = Path(file_path)

    if not path.exists():
        print(f"Error: File '{file_path}' not found.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    total_words = count_words(content)

    print(f"\n{'='*60}")
    print(f"Patent Document Analysis: {path.name}")
    print(f"{'='*60}")
    print(f"\nTotal word count: {total_words}")

    # Check if it's an abstract
    if 'abstract' in path.name.lower():
        print(f"\nAbstract Requirements:")
        print(f"  Maximum allowed: 150 words")
        print(f"  Current count: {total_words}")
        if total_words <= 150:
            print(f"  Status: ✓ Within limit ({150 - total_words} words remaining)")
        else:
            print(f"  Status: ✗ EXCEEDS limit by {total_words - 150} words")

    # Check for sections if it's a full application
    sections = {
        'Background': r'##\s+BACKGROUND',
        'Summary': r'##\s+.*SUMMARY',
        'Description': r'##\s+.*DESCRIPTION',
        'Claims': r'##\s+CLAIMS',
        'Abstract': r'##\s+ABSTRACT'
    }

    print(f"\nDocument Structure:")
    for section_name, pattern in sections.items():
        if re.search(pattern, content, re.IGNORECASE):
            print(f"  ✓ {section_name} section found")
        else:
            print(f"  - {section_name} section not found")

    print(f"\n{'='*60}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python word-count.py <file_path>")
        print("Example: python word-count.py ../templates/abstracts/my-abstract.md")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_patent_document(file_path)


if __name__ == "__main__":
    main()
