#!/usr/bin/env python3
"""Wrapper de retrocompatibilidad para validate_organization_analysis.py."""

import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(script_dir))

from validate_organization_analysis import main

if __name__ == "__main__":
    main()
