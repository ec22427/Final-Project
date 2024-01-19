import unittest
import pandas as pd

class TestKpopChartsAndSales(unittest.TestCase):

    def setUp(self):
        # Load and clean the data for testing
        file_path = "test_dataset.csv"  # Create a smaller test dataset for unit testing
        self.df = load_and_clean_data(file_path)
         
         
    def test_load_and_clean_data(self):
        # Check if the loaded DataFrame has the expected columns
        expected_columns = ['Artist', 'title', 'date', 'country', 'sales', 'peak_chart']
        self.assertListEqual(list(self.df.columns), expected_columns)

        # Check if 'sales' column contains only numeric values
        self.assertTrue(self.df['sales'].apply(lambda x: pd.to_numeric(x, errors='coerce')).notna().all())
        
    def test_display_basic_info(self):
        # Ensure that the function doesn't raise any exceptions
        try:
            display_basic_info(self.df)
        except Exception as e:
            self.fail(f"display_basic_info raised an exception: {str(e)}")
            
    def test_visualise_peak_chart(self):
        # Ensure that the function doesn't raise any exceptions
        try:
            visualise_peak_chart(self.df)
        except Exception as e:
            self.fail(f"visualise_peak_chart raised an exception: {str(e)}")




