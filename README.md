# Customer Churn Prediction using XGBoost, MLflow & SHAP

![Python](https://img.shields.io/badge/Python-3.10-blue)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Model-success)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

## Model Performance

| Metric    | Score    |
| --------- | -------- |
| AUC-ROC   | **0.91** |
| Precision | **0.89** |
| Recall    | **0.79** |
| F1 Score  | **0.84** |


# Project Overview

This project predicts customer churn for a telecom company using machine learning and explainable AI techniques.

The system includes:

* End-to-end ML pipeline
* Feature engineering
* XGBoost model training
* MLflow experiment tracking
* SHAP explainability
* FastAPI deployment
* Streamlit dashboard
* Docker support

---

# Business Problem

Customer churn directly impacts revenue and customer acquisition costs.

The objective of this project is to:

* Predict high-risk customers
* Understand key churn drivers
* Help businesses improve customer retention strategies

---

# Key Business Insights (SHAP Explainability)

### Top churn drivers identified:

* Month-to-month contracts are the **#1 churn driver** (SHAP impact: 0.31)
* Customers without online security churn **2.4x more**
* High monthly charges significantly increase churn probability
* Long-term contract customers show much lower churn risk

These insights help business teams design targeted retention campaigns.

---

# Tech Stack

* Python
* Pandas
* Scikit-learn
* XGBoost
* MLflow
* SHAP
* FastAPI
* Streamlit
* Docker

---

# Project Architecture

```bash
customer-churn-prediction/
│
├── data/
├── notebooks/
├── src/
├── pipeline/
├── models/
├── reports/
├── api/
├── dashboard/
├── deployment/
├── tests/
├── configs/
└── mlruns/
```

---

# Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/sahithiroy/customer-churn--prediction.git

cd customer-churn--prediction
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Training Pipeline

```bash
python pipeline/training_pipeline.py
```

---

# Run MLflow Tracking UI

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

---

# Run Streamlit Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

---

# Run FastAPI Server

```bash
uvicorn api.app:app --reload
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Model Pipeline

The training pipeline performs:

1. Data ingestion
2. Data preprocessing
3. Feature engineering
4. Train-test split
5. XGBoost model training
6. MLflow logging
7. Model evaluation
8. Model persistence

---

# Explainability with SHAP

SHAP values are used to explain model predictions and identify the most influential customer attributes contributing to churn.

Generated outputs:

* SHAP summary plots
* Feature importance rankings
* Individual prediction explanations

---

# Future Improvements

* Hyperparameter optimization with Optuna
* CI/CD pipeline integration
* Kubernetes deployment
* Real-time prediction API
* Drift monitoring

---

# Author

## Lakshmi Sahithi Sugavasi

Data Analyst | Machine Learning Engineer | AI Enthusiast

GitHub:
https://github.com/sahithiroy


