from fastapi import FastAPI

from pipeline.prediction_pipeline import PredictionPipeline
from api.schema import CustomerData, PredictionResponse

app = FastAPI()

prediction_pipeline = PredictionPipeline()


@app.post("/predict")
def predict(customer_data: CustomerData):

    predictions, probabilities = prediction_pipeline.run(
        customer_data
    )

    return PredictionResponse(
        id=customer_data.id,
        prediction=int(predictions[0]),
        churn_probability=float(probabilities[0])
    )