from src.data_ingestion import DataIngestion

from src.feature_engineering import FeatureEngineering

from src.data_preprocessing import DataPreprocessing

from src.model_training import ModelTraining

from src.evaluation import ModelEvaluation

from src.prediction import Prediction

from src.utils import Utils

import numpy as np

import mlflow

import mlflow.sklearn

import mlflow.xgboost


class TrainingPipeline:

    def __init__(self):

        self.utils = Utils()

    def run(self):

        print("Training Pipeline Started")

        # -----------------------------------------
        # DATA INGESTION
        # -----------------------------------------

        ingestion = DataIngestion(

            "data/raw/train.csv"
        )

        df = ingestion.ingest_data()

        # -----------------------------------------
        # FEATURE ENGINEERING
        # -----------------------------------------

        feature_engineering = FeatureEngineering(df)

        df = feature_engineering.engineer_features()

        # -----------------------------------------
        # DATA PREPROCESSING
        # -----------------------------------------

        preprocessing = DataPreprocessing(df)

        X_train, X_test, y_train, y_test, preprocessor = preprocessing.preprocess()

        # -----------------------------------------
        # MODEL TRAINING
        # -----------------------------------------

        trainer = ModelTraining()

        trained_models = trainer.train_models(

            X_train,

            y_train
        )

        # -----------------------------------------
        # MODEL EVALUATION
        # -----------------------------------------

        evaluation = ModelEvaluation()

        # -----------------------------------------
        # BEST MODEL TRACKING
        # -----------------------------------------

        best_model = None

        best_model_name = None

        best_auc = 0

        # -----------------------------------------
        # LOOP THROUGH ALL MODELS
        # -----------------------------------------

        for model_name, model in trained_models.items():

            print(f"\nTraining Completed for {model_name}")

            # -----------------------------------------
            # START MLFLOW RUN
            # -----------------------------------------

            with mlflow.start_run(run_name=model_name):

                print(f"\nMLflow Tracking Started for {model_name}")

                # -----------------------------------------
                # EVALUATE MODEL
                # -----------------------------------------

                metrics = evaluation.evaluate(

                    model,

                    X_test,

                    y_test
                )

                # -----------------------------------------
                # LOG PARAMETERS
                # -----------------------------------------

                mlflow.log_param(

                    "model_name",

                    model_name
                )

                # Logistic Regression Parameters
                if model_name == "LogisticRegression":

                    mlflow.log_param(

                        "solver",

                        model.solver
                    )

                # Random Forest Parameters
                elif model_name == "RandomForest":

                    mlflow.log_param(

                        "n_estimators",

                        model.n_estimators
                    )

                    mlflow.log_param(

                        "max_depth",

                        model.max_depth
                    )

                # XGBoost Parameters
                elif model_name == "XGBoost":

                    mlflow.log_param(

                        "n_estimators",

                        model.n_estimators
                    )

                    mlflow.log_param(

                        "learning_rate",

                        model.learning_rate
                    )

                    mlflow.log_param(

                        "max_depth",

                        model.max_depth
                    )

                # -----------------------------------------
                # LOG METRICS
                # -----------------------------------------

                for key, value in metrics.items():

                    mlflow.log_metric(

                        key,

                        value
                    )

                if model_name == "XGBoost":

                    mlflow.xgboost.log_model(

                        model,

                        "model"
                    )

                else:

                    mlflow.sklearn.log_model(

                        model,

                        "model"
                    )

                print(f"MLflow Logging Completed for {model_name}")

                # -----------------------------------------
                # BEST MODEL SELECTION
                # -----------------------------------------

                if metrics['roc_auc'] > best_auc:

                    best_auc = metrics['roc_auc']

                    best_model = model

                    best_model_name = model_name

        # -----------------------------------------
        # PRINT BEST MODEL
        # -----------------------------------------

        print("\nBest Model Selected")

        print(f"Best Model: {best_model_name}")

        print(f"Best ROC AUC: {best_auc:.4f}")

        # -----------------------------------------
        # SAVE BEST MODEL
        # -----------------------------------------

        self.utils.save_model(

            best_model,

            "models/churn_model.pkl"
        )

        # Save preprocessor
        self.utils.save_model(

            preprocessor,

            "models/preprocessor.pkl"
        )

        print("Best Model Saved Successfully")

        # -----------------------------------------
        # TEST PREDICTION PIPELINE
        # -----------------------------------------

        prediction_pipeline = Prediction()

        predictions, probabilities = prediction_pipeline.predict(
            X_test
        )

        print("\nPrediction Pipeline Executed Successfully")

        print("\nCustomers likely to churn:")

        print(np.where(predictions == 1)[0].size)

        print("\nCustomers likely to stay:")

        print(np.where(predictions == 0)[0].size)

        print("\nTraining Pipeline Completed Successfully")


if __name__ == "__main__":

    pipeline = TrainingPipeline()

    pipeline.run()