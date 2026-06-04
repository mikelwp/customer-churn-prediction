# Customer Churn Prediction using Machine Learning

Predicting customer churn is a critical business problem that helps companies identify customers who are likely to stop using their services. Early prediction enables businesses to implement retention strategies and reduce customer loss.

This project develops a machine learning pipeline to predict customer churn using the IBM Telco Customer Churn dataset. The workflow includes data preprocessing, exploratory data analysis (EDA), model training, hyperparameter tuning, and model evaluation.

---

## Project Overview

### Objective

Predict whether a customer is likely to churn based on demographic information, account details, and subscribed services.

### Dataset

https://www.kaggle.com/code/emineyetm/telco-customer-churn?select=WA_Fn-UseC_-Telco-Customer-Churn.csv

* 7,043 customer records
* 30 predictive features
* Binary classification target:

  * 0 = Customer stays
  * 1 = Customer churns

---

## Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. One-Hot Encoding
6. Train-Test Split
7. Model Training
8. Hyperparameter Tuning
9. Model Evaluation
10. Feature Importance Analysis
11. Model Deployment Preparation

---

## Technologies Used

| Category                | Tools               |
| ----------------------- | ------------------- |
| Programming Language    | Python              |
| Data Processing         | Pandas, NumPy       |
| Visualization           | Matplotlib, Seaborn |
| Machine Learning        | Scikit-Learn        |
| Development Environment | Jupyter Notebook    |
| Deployment              | Streamlit           |

---

## Models Evaluated

### Logistic Regression

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 80.41% |
| Precision | 66%    |
| Recall    | 55%    |
| F1-Score  | 60%    |
| ROC-AUC   | 84.25% |

### Random Forest (Default)

| Metric   | Score  |
| -------- | ------ |
| Accuracy | 78.64% |
| ROC-AUC  | 82.51% |

### Random Forest (Tuned)

Best Parameters:

```python
{
    'max_depth': 10,
    'min_samples_leaf': 2,
    'min_samples_split': 5,
    'n_estimators': 100
}
```

Performance:

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 80.34% |
| Precision | 66%    |
| Recall    | 53%    |
| F1-Score  | 59%    |

---

## Feature Importance

Top influential features identified by the tuned Random Forest model:

1. Tenure
2. Total Charges
3. Monthly Charges
4. Internet Service (Fiber Optic)
5. Electronic Check Payment Method
6. Contract Type
7. Online Security
8. Technical Support

### Key Insights

* Customers with shorter tenure are more likely to churn.
* Higher monthly charges contribute to increased churn risk.
* Long-term contracts significantly reduce churn probability.
* Additional services such as Online Security and Tech Support improve customer retention.

---

## Project Structure

```text
customer-churn-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── customer_churn_prediction.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/mikelwp/customer-churn-prediction.git
cd customer-churn-prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app/app.py
```

---

## Future Improvements

* Streamlit Dashboard
* SHAP Explainability
* Customer Retention Recommendation System
* Model Monitoring
* Cloud Deployment

---

## Author

Michael William
