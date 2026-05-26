import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class DataPreprocessing:

    def __init__(self, df):

        self.df = df.copy()

    def preprocess(self):

        print("Starting Preprocessing...")

        # Convert TotalCharges to numeric
        self.df['TotalCharges'] = pd.to_numeric(
            self.df['TotalCharges'],
            errors='coerce'
        )

        # Fill missing values
        self.df['TotalCharges'].fillna(
            self.df['TotalCharges'].median(),
            inplace=True
        )

        # Encode target
        self.df['Churn'] = self.df['Churn'].map({
            'Yes': 1,
            'No': 0
        })

        # Split features and target
        X = self.df.drop('Churn', axis=1)

        y = self.df['Churn']

        # Numerical columns
        numerical_cols = X.select_dtypes(
            include=['int64', 'float64']
        ).columns

        # Categorical columns
        categorical_cols = X.select_dtypes(
            include=['object']
        ).columns

        # Numerical transformer
        numerical_transformer = Pipeline(
            steps=[
                ('scaler', StandardScaler())
            ]
        )

        # Categorical transformer
        categorical_transformer = Pipeline(
            steps=[
                (
                    'encoder',
                    OneHotEncoder(handle_unknown='ignore')
                )
            ]
        )

        # Combine preprocessing
        preprocessor = ColumnTransformer(

            transformers=[

                (
                    'num',
                    numerical_transformer,
                    numerical_cols
                ),

                (
                    'cat',
                    categorical_transformer,
                    categorical_cols
                )
            ]
        )

        # Train test split
        X_train, X_test, y_train, y_test = train_test_split(

            X,
            y,

            test_size=0.2,
            random_state=42,
            stratify=y
        )

        # Apply preprocessing
        X_train_processed = preprocessor.fit_transform(
            X_train
        )

        X_test_processed = preprocessor.transform(
            X_test
        )

        print("Preprocessing Completed")

        return (

            X_train_processed,
            X_test_processed,

            y_train,
            y_test,

            preprocessor
        )