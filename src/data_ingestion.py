# Import pandas library
import pandas as pd
from src.utils import Utils
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
        self.utils = Utils()


    def ingest_data(self)-> pd.DataFrame:

        # Read CSV file
        df= self.utils.load_dataFrame(self.file_path)

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
        if df.isnull().sum().sum() > 0:
            print("\nNull values found in the dataset. Consider handling them before proceeding.")
            df = self.fill_null_values(df)
        

        # Return dataframe
        return df
    def fill_null_values(self, df: pd.DataFrame) -> pd.DataFrame:
        '''        This method fills null values in the DataFrame with the mean of the respective columns.
        Parameters:            df (pd.DataFrame): The input DataFrame with potential null values.
        Returns:            pd.DataFrame: The DataFrame with null values filled.
        '''
        # Fill null values with mean of respective columns
        