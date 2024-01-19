import unittest
import pandas as pd

class TestKpopChartsAndSales(unittest.TestCase):

    def setUp(self):
        # Load and clean the data for testing
        file_path = "test_dataset.csv"  # Create a smaller test dataset for unit testing
        self.df = load_and_clean_data(file_path)
