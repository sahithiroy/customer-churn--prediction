import joblib


class PredictionPipeline:

    def __init__(self):

        self.model = joblib.load(
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