from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier


class ModelTraining:

    def __init__(self):

        self.models = {

            "LogisticRegression": LogisticRegression(),

            "RandomForest": RandomForestClassifier(

                n_estimators=200,

                random_state=42
            ),

            "XGBoost": XGBClassifier(

                n_estimators=300,

                learning_rate=0.05,

                max_depth=4,

                random_state=42
            )
        }

    def train_models(

        self,

        X_train,

        y_train
    ):

        trained_models = {}

        for name, model in self.models.items():

            print(f"\nTraining {name}...")

            model.fit(

                X_train,

                y_train
            )

            trained_models[name] = model

            print(f"{name} Training Completed")

        return trained_models