import unittest
import pandas as pd
from cleanmydata import DataClean

class TestDataClean(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'Name': [' John ', ' Jane ', ' Bob '],
                'Age': [25, None, 35],
                'Email': ['john@example.com', 'jane@example.com', 'bob@example.com']}
        self.df = pd.DataFrame(data)

    def test_clean_data(self):
        # Initialize DataClean instance with sample DataFrame
        cleaner = DataClean(self.df)

        # Clean all text columns
        cleaned_df = cleaner.clean_data(columns='all')

        # Verify that text columns have been cleaned and lowercase
        self.assertEqual(cleaned_df['Name'].tolist(), ['john', 'jane', 'bob'])
        self.assertEqual(cleaned_df['Email'].tolist(), ['john@example.com', 'jane@example.com', 'bob@example.com'])

    def test_handle_missing_values(self):
        # Initialize DataClean instance with sample DataFrame
        cleaner = DataClean(self.df)

        # Handle missing values by replacing with 'Unknown' in the 'Age' column
        missing_values = {'Age': 'replace missing value with Unknown'}
        cleaned_df = cleaner.handle_missing_values(missing_values)

        # Verify that missing values have been replaced
        self.assertEqual(cleaned_df['Age'].tolist(), [25, 'Unknown', 35])

    def test_explode_data(self):
        # Initialize DataClean instance with sample DataFrame
        cleaner = DataClean(self.df)

        # Explode the 'Name' column
        explode_columns = {'Name': ' '}
        exploded_df = cleaner.explode_data(explode_columns)

        # Verify that the 'Name' column has been exploded

        # TODO: Add assertions based on your specific explode implementation

    def test_parse_date_column(self):
        # Initialize DataClean instance with sample DataFrame
        cleaner = DataClean(self.df)

        # Parse the 'Age' column as a date column
        date_columns = ['Age']
        parsed_df = cleaner.parse_date_column(date_columns)

        # Verify that the 'Age' column has been parsed as a date column

        # TODO: Add assertions based on your specific date parsing implementation

    def test_translate_columns(self):
        # Initialize DataClean instance with sample DataFrame
        cleaner = DataClean(self.df)

        # Translate the 'Name' column
        translations = {'Name': True}
        translated_df = cleaner.translate_columns(translations)

        # Verify that the 'Name' column has been translated

        # TODO: Add assertions based on your specific translation implementation

    def test_prep(self):
        # Initialize DataClean instance with sample DataFrame
        cleaner = DataClean(self.df)

        # Define parameters for the prep function
        clean_columns = 'all'
        missing_values = {'Age': 'replace missing value with Unknown'}
        perform_scaling_normalization_bool = False
        explode_columns = {'Name': ' '}
        date_columns = ['Age']
        translations = {'Name': True}

        # Perform the preparation steps
        prepared_df = cleaner.prep(clean=clean_columns,
                                   missing_values=missing_values,
                                   perform_scaling_normalization=perform_scaling_normalization_bool,
                                   explode_columns=explode_columns,
                                   date_columns=date_columns,
                                   translations=translations)

        # Verify the final prepared DataFrame

        # TODO: Add assertions based on your specific data preparation implementation

if __name__ == '__main__':
    unittest.main()
