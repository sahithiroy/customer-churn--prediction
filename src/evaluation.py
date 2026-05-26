from sklearn.metrics import (

    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


class ModelEvaluation:

    def evaluate(

        self,

        model,

        X_test,

        y_test
    ):

        predictions = model.predict(X_test)

        probabilities = model.predict_proba(
            X_test
        )[:, 1]

        accuracy = accuracy_score(

            y_test,
            predictions
        )

        precision = precision_score(

            y_test,
            predictions
        )

        recall = recall_score(

            y_test,
            predictions
        )

        f1 = f1_score(

            y_test,
            predictions
        )

        auc = roc_auc_score(

            y_test,
            probabilities
        )

        print("Model Evaluation")

        print(f"Accuracy : {accuracy:.4f}")

        print(f"Precision: {precision:.4f}")

        print(f"Recall   : {recall:.4f}")

        print(f"F1 Score : {f1:.4f}")

        print(f"ROC AUC  : {auc:.4f}")

        return {

            'accuracy': accuracy,

            'precision': precision,

            'recall': recall,

            'f1_score': f1,

            'roc_auc': auc
        }