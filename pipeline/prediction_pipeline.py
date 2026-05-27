import pandas as pd

from src.feature_engineering import FeatureEngineering
from src.data_preprocessing import DataPreprocessing
from src.prediction import Prediction
from src.utils import Utils



class PredictionPipeline:

    def __init__(self):

        self.utils = Utils()

    def run(self, customer_data):

        print("Prediction Pipeline Started")

        # Convert API request to dataframe
        df = pd.DataFrame([{

            "id": customer_data.id,
            "gender": customer_data.gender.value,
            "SeniorCitizen": customer_data.senior_citizen.value,
            "Partner": customer_data.partner.value,
            "Dependents": customer_data.dependents.value,
            "tenure": customer_data.tenure,
            "PhoneService": customer_data.phone_service.value,
            "MultipleLines": customer_data.multiple_lines.value,
            "InternetService": customer_data.internet_service.value,
            "OnlineSecurity": customer_data.online_security.value,
            "OnlineBackup": customer_data.online_backup.value,
            "DeviceProtection": customer_data.device_protection.value,
            "TechSupport": customer_data.tech_support.value,
            "StreamingTV": customer_data.streaming_tv.value,
            "StreamingMovies": customer_data.streaming_movies.value,
            "Contract": customer_data.contract_type.value,
            "PaperlessBilling": "Yes",
            "PaymentMethod": customer_data.payment_method.value,
            "MonthlyCharges": customer_data.monthly_charges,
            "TotalCharges": customer_data.total_charges
        }])

        print(df.head())

        # Feature Engineering
        feature_engineering = FeatureEngineering(df)

        df = feature_engineering.engineer_features()

        # Preprocessing
        preprocessing = DataPreprocessing(df)

        processed_data = preprocessing.preprocess(
            training=False
        )

        # Prediction
        prediction = Prediction()

        predictions, probabilities = prediction.predict(
            processed_data
        )

        print(predictions)
        print(probabilities)

        return predictions, probabilities