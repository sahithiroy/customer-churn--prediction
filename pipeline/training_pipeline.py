from src.data_ingestion import DataIngestion

from src.feature_engineering import FeatureEngineering

from src.data_preprocessing import DataPreprocessing

from src.model_training import ModelTraining

from src.evaluation import ModelEvaluation


# Data ingestion
ingestion = DataIngestion(

    "data/raw/train.csv"
)

df = ingestion.ingest_data()

# Feature engineering
fe = FeatureEngineering(df)

df = fe.engineer_features()

# Preprocessing
preprocessing = DataPreprocessing(df)

X_train, X_test, y_train, y_test, preprocessor = preprocessing.preprocess()


# Model training
trainer = ModelTraining()

model = trainer.train_model(

    X_train,
    y_train
)

# Evaluation
evaluation = ModelEvaluation()

metrics = evaluation.evaluate(

    model,

    X_test,

    y_test
)