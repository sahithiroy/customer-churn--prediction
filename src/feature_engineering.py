import pandas as pd


class FeatureEngineering:

    def __init__(self, df):

        self.df = df.copy()

    def engineer_features(self):

        print("Starting Feature Engineering...")

        # Average spend
        self.df['avg_monthly_spend'] = (

            self.df['TotalCharges'] /

            (self.df['tenure'] + 1)
        )

        # Tenure groups
        self.df['tenure_group'] = pd.cut(

            self.df['tenure'],

            bins=[0, 12, 24, 48, 72],

            labels=[0, 1, 2, 3]

        ).astype(int)

        # Service count
        service_cols = [

            'OnlineSecurity',
            'TechSupport',
            'OnlineBackup',
            'DeviceProtection',
            'StreamingTV',
            'StreamingMovies'
        ]

        self.df['service_count'] = self.df[
            service_cols
        ].apply(

            lambda row: (row == 'Yes').sum(),

            axis=1
        )

        # High-value customer
        self.df['is_high_value'] = (

            (

                self.df['MonthlyCharges'] > 70

            ) &

            (

                self.df['tenure'] > 24
            )

        ).astype(int)

        print("Feature Engineering Completed")

        return self.df