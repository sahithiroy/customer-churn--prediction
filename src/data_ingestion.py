# Import pandas library
import pandas as pd

# Create DataIngestion class
class DataIngestion:
    '''
    This class is responsible for ingesting data from a CSV file.
    Attributes:    file_path (str): The path to the CSV file to be ingested.
    Methods:    ingest_data(): Reads the CSV file, displays basic information about the dataset, and returns a pandas DataFrame.    
    returns:    pandas.DataFrame: The ingested dataset as a DataFrame.
    '''

    # Constructor
    def __init__(self, file_path):
        self.file_path = file_path

    def ingest_data(self)-> pd.DataFrame:

        # Read CSV file
        df = pd.read_csv(self.file_path)

        # Display first 5 rows
        print("First 5 Rows of Dataset:")
        print(df.head())

        # Shape of dataset
        print("\nShape of Dataset:")
        print(df.shape)

        # Dataset information
        print("\nDataset Information:")
        print(df.info())

        # Check null values
        print("\nNull Values:")
        print(df.isnull().sum())

        # Return dataframe
        return df
