import pandas as pd
import unittest

# Load the CSV file
file_path = 'library_books_dataset.csv'

# Read the CSV file, skipping the first row
books_df = pd.read_csv(file_path, skiprows=1, names=['book_ID', 'title', 'author', 'genre', 'publication', 'availability'])

# Display the first few rows of the dataframe to ensure it has been read correctly
print(books_df.head())
