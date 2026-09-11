#!/usr/bin/env python3
"""Punto de entrada para ejecución de pruebas unitarias de sipocBuilder en carpeta tests/."""

import os
import sys
import unittest

# Asegurar importación determinista
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from test_validate_sipoc import TestSipocValidator

if __name__ == "__main__":
    unittest.main()
