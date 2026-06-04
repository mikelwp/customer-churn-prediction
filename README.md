# Customer Churn Prediction Using Machine Learning

## Overview

Customer churn prediction is a machine learning task that aims to identify customers who are likely to stop using a service. Early churn prediction allows companies to take preventive actions and improve customer retention.

This project develops and evaluates machine learning models to predict customer churn using the IBM Telco Customer Churn dataset. The project includes data preprocessing, exploratory data analysis (EDA), model training, hyperparameter tuning, and model evaluation.

---

## Dataset

Dataset: IBM Telco Customer Churn Dataset

The dataset contains customer demographic information, subscription details, account information, and churn status.

### Target Variable

* Churn = 1 → Customer leaves the service
* Churn = 0 → Customer remains with the service

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Feature Encoding
6. Train-Test Split
7. Model Training
8. Hyperparameter Tuning
9. Model Evaluation
10. Feature Importance Analysis

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Machine Learning Models

### Logistic Regression

Used as the baseline classification model.

Performance:

* Accuracy: 80.41%
* ROC-AUC: 84.25%

### Random Forest

Performance before tuning:

* Accuracy: 78.64%
* ROC-AUC: 82.51%

### Tuned Random Forest

Hyperparameter tuning was performed using GridSearchCV.

Best Parameters:

```python
{
    'max_depth': 10,
    'min_samples_leaf': 2,
    'min_samples_split': 5,
    'n_estimators': 100
}
```

Performance after tuning:

* Accuracy: 80.34%

---

## Model Evaluation

### Logistic Regression

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 80.41% |
| Precision | 66%    |
| Recall    | 55%    |
| F1-Score  | 60%    |
| ROC-AUC   | 84.25% |

### Tuned Random Forest

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 80.34% |
| Precision | 66%    |
| Recall    | 53%    |
| F1-Score  | 59%    |

---

## Key Findings

The results show that Logistic Regression slightly outperformed Random Forest on this dataset.

This suggests that customer churn behavior in the Telco dataset can be effectively captured using a relatively simple linear classification model.

---

## Repository Structure

```text
customer-churn-prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── notebooks/
│   └── customer_churn_prediction.ipynb
│
├── models/
│   └── churn_model.pkl
│
├── app/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Improvements

* Streamlit Deployment
* SHAP Explainability
* Feature Importance Visualization
* Model Comparison Dashboard
* Customer Retention Recommendation System

---

## Author
Michael William

