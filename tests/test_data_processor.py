import unittest
import pandas as pd
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def test_transform_data(self):
        data = {'DOB': ['06031987'], 'Last_Consulted_Date': ['20121013']}
        df = pd.DataFrame(data)
        transformed = DataProcessor.transform_data(df)
        self.assertIn('Age', transformed.columns)
        self.assertIn('Days_Since_Last_Consulted', transformed.columns)

    def test_split_by_country(self):
        data = {'Country': ['USA', 'IND'], 'Customer_Name': ['Alex', 'John']}
        df = pd.DataFrame(data)
        split = DataProcessor.split_by_country(df)
        self.assertEqual(len(split), 2)

if __name__ == "__main__":
    unittest.main()
