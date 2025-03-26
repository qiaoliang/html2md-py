#!/usr/bin/env python3
"""Command-line entry point for html-to-markdown."""

import sys

from html_to_markdown.cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
