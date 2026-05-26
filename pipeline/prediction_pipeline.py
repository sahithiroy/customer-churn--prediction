from src.data_ingestion import DataIngestion

from src.feature_engineering import FeatureEngineering
from src.utils import Utils
from src.data_preprocessing import DataPreprocessing

from src.prediction import Prediction
import numpy as np
class PredictionPipeline:

    def __init__(self):
        self.utils = Utils()
    def run(self):
        ingestion = DataIngestion(
            "data/raw/test.csv"
        )

        df = ingestion.ingest_data()

        feature_engineering = FeatureEngineering(df)

        df = feature_engineering.engineer_features()

        preprocessing = DataPreprocessing(df)

        processed_data = preprocessing.preprocess(
            training=False
        )


        prediction_pipeline = Prediction()


        predictions, probabilities = prediction_pipeline.predict(
            processed_data
        )


        print("Predictions:")
        print(predictions)

        print("\nProbabilities:")
        print(probabilities)
        print("Prediction Pipeline Executed Successfully")
        print(np.where(predictions == 1)[0].size)
        print(np.where(predictions == 0)[0].size)
if __name__ == "__main__":
    pipeline = PredictionPipeline()
    pipeline.run()