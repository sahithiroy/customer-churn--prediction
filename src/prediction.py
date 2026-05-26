import joblib
from src.utils import Utils

class Prediction:

    def __init__(self):
        self.utils = Utils()

        self.model = self.utils.load_model(
            'models/churn_model.pkl'
        )

    def predict(

        self,

        data
    ):

        prediction = self.model.predict(data)

        probability = self.model.predict_proba(
            data
        )[:, 1]

        return prediction, probability