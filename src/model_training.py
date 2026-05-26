from xgboost import XGBClassifier


class ModelTraining:

    def __init__(self):

        self.model = XGBClassifier(

            n_estimators=300,

            learning_rate=0.05,

            max_depth=4,

            random_state=42
        )

    def train_model(

        self,

        X_train,

        y_train
    ):

        print("Training Model...")

        self.model.fit(

            X_train,
            y_train
        )

        print("Model Training Completed")

        return self.model