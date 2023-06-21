## DataClean

The `DataClean` class provides a set of methods to clean and process data in a pandas DataFrame. It includes functions for cleaning text data, handling missing values, performing scaling normalization, exploding data, parsing date columns, and translating text columns.

### Class Initialization

To create an instance of the `DataClean` class, you need to provide the filepath of the data file (CSV or Excel) as an argument to the constructor. The class will automatically read the data into a pandas DataFrame based on the file extension.

Example:
```python
cleaner = DataClean('data.csv')
```

### Method: clean_data

The `clean_data` method cleans text data in the DataFrame. It takes a parameter `columns` that specifies which columns to clean. You can either pass `'all'` to clean all columns or provide a list of specific column names to clean.

Example:
```python
cleaned_data = cleaner.clean_data(['text_column1', 'text_column2'])
```

### Method: handle_missing_values

The `handle_missing_values` method handles missing values in the DataFrame. It takes a parameter `missing_values`, which is a dictionary specifying the actions to be taken for each column with missing values. The keys of the dictionary are the column names, and the values are the operations to be performed.

Example:
```python
missing_values = {'column1': 'replace missing value with 0', 'column2': 'drop'}
processed_data = cleaner.handle_missing_values(missing_values)
```

### Method: perform_scaling_normalization

The `perform_scaling_normalization` method performs scaling normalization on numerical columns in the DataFrame using the Box-Cox transformation. Currently, this method is marked as 'NOT COMPLETE' in the code and does not contain the complete implementation.

### Method: explode_data

The `explode_data` method splits and expands data in specified columns of the DataFrame. It takes a dictionary `explode` where the keys are column names, and the values are the separators for splitting.

Example:
```python
explode_columns = {'column1': ',', 'column2': ';'}
exploded_data = cleaner.explode_data(explode_columns)
```

### Method: dupli

The `dupli` method removes duplicate rows from the DataFrame.

Example:
```python
unique_data = cleaner.dupli()
```

### Method: parse_date_column

The `parse_date_column` method converts specified columns in the DataFrame to datetime format and formats them as 'YYYY-MM-DD'. It takes a list `date_columns` containing the names of the columns to be converted.

Example:
```python
date_columns = ['date_column1', 'date_column2']
parsed_data = cleaner.parse_date_column(date_columns)
```

### Method: translate_columns

The `translate_columns` method translates text in specified columns of the DataFrame to English using Google Translate. It takes a dictionary `translations` where the keys are column names, and the values are overwrite boolean values. If the overwrite value is True, the original column will be overwritten; otherwise, a new column with the translated text will be added.

Example:
```python
column_translations = {'text_column1': True, 'text_column2': False}
translated_data = cleaner.translate_columns(column_translations)
```

### Method: prep

The `prep` method is the main function to prepare and clean the DataFrame. It provides a convenient way to perform multiple cleaning and processing operations in a specific order. You can specify the operations using the following parameters:

- `clean`: Columns to clean. Pass `'all'` to clean all columns or provide a list of specific column names.
- `missing_values`: Actions

 to be taken on missing values. Pass a dictionary with column names as keys and operations as values.
- `perform_scaling_normalization_bool`: Boolean value indicating whether to perform scaling normalization on numerical columns.
- `explode`: Columns to be exploded. Pass a dictionary with column names as keys and separators for splitting as values.
- `parse_date`: List of column names to be converted to datetime format.
- `translate_column_names`: Dictionary mapping column names to overwrite boolean values for translation.

Example:
```python
cleaned_data = cleaner.prep(clean='all', missing_values={'column1': 'drop'}, perform_scaling_normalization_bool=True, explode={'column2': ','}, parse_date=['date_column1'], translate_column_names={'text_column1': True})
```

### Getting the Cleaned DataFrame

To obtain the cleaned and processed DataFrame, you can call the `prep` method and assign the returned DataFrame to a variable.

Example:
```python
cleaned_data = cleaner.prep(clean='all', missing_values={'column1': 'drop'})
```

The variable `cleaned_data` will contain the final cleaned and processed DataFrame.

Please note that some methods in the code are marked as 'NOT COMPLETE' and require further implementation to work properly. You can modify and complete those methods as per your requirements.