#!/usr/bin/env python3
"""Runner de compatibilidad para pruebas de organizationAnalysis."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_validate_organization_analysis import TestValidateOrganizationAnalysis

if __name__ == "__main__":
    unittest.main()
