import shap
import matplotlib.pyplot as plt


class Explainability:

    def generate_shap_summary(

        self,

        model,

        X_train
    ):

        print("Generating SHAP Summary Plot...")

        explainer = shap.TreeExplainer(model)

        shap_values = explainer.shap_values(
            X_train
        )

        shap.summary_plot(

            shap_values,

            X_train
        )

        plt.show()