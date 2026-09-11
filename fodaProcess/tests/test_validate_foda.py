#!/usr/bin/env python3
"""Punto de entrada de pruebas unitarias para fodaProcess en carpeta tests/."""

import os
import sys
import unittest

# Asegurar importación determinista
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from test_validate_foda import TestFodaValidator

if __name__ == "__main__":
    unittest.main()
