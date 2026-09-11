import importlib.util
import os
import unittest

script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts", "test_validate_sipoc.py"))
spec = importlib.util.spec_from_file_location("sipoc_script_tests", script_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TestSipocValidator = mod.TestSipocValidator

if __name__ == "__main__":
    unittest.main()
