# test_matplotlibplots.py
"""
Tests for MatplotlibPlots module.
"""

import unittest
from matplotlibplots import MatplotlibPlots

class TestMatplotlibPlots(unittest.TestCase):
    """Test cases for MatplotlibPlots class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MatplotlibPlots()
        self.assertIsInstance(instance, MatplotlibPlots)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MatplotlibPlots()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
