import os
import joblib
import pandas as pd
class Utils:
    def create_directory_if_not_exists(self, path):
        
        if not os.path.exists(path):
            os.makedirs(path)
    def save_model(self, model, path):
        self.create_directory_if_not_exists(os.path.dirname(path))
        joblib.dump(model, path)
        print(f"Model saved to {path}")
    def load_model(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model file not found at {path}")
        model = joblib.load(path)
        print(f"Model loaded from {path}")
        return model
    def save_dataFrame(self, df, path):
        self.create_directory_if_not_exists(os.path.dirname(path))
        df.to_csv(path, index=False)
        print(f"DataFrame saved to {path}")
    def load_dataFrame(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Data file not found at {path}")
        df = pd.read_csv(path)
        print(f"DataFrame loaded from {path}")
        return df

