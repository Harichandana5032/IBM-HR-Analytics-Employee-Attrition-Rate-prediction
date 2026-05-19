# IBM-HR-Analytics-Employee-Attrition-Rate-prediction
AI-powered HR Analytics project focused on predicting employee attrition using Machine Learning. Built with Python, Scikit-learn, SHAP, and Power BI to identify key attrition drivers through EDA, predictive modeling, explainable AI, and interactive dashboards for HR decision-making.
# IBM HR Analytics — Predict Employee Attrition

## Project Overview

This project focuses on analyzing employee attrition using Machine Learning and Data Analytics techniques. The objective is to identify the major factors influencing employee resignations and build a predictive model that helps HR departments proactively retain employees.

The project uses the IBM HR Analytics dataset containing employee-related information such as salary, overtime, work-life balance, job role, age, and performance metrics.

---

## Problem Statement

Employee attrition creates major challenges for organizations including:

- Increased recruitment and training costs
- Loss of experienced employees
- Reduced productivity
- Knowledge transfer issues

The main goal of this project is to answer:

> "Which employees are most likely to leave the organization, and what factors are driving attrition?"

---

## Dataset Information

- Dataset: IBM HR Analytics Dataset
- Total Records: 1,470 employees
- Total Features: 35 columns
- Target Variable: Attrition

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Exploratory Data Analysis |
| Scikit-learn | Machine Learning |
| SMOTE | Handling Class Imbalance |
| SHAP | Explainable AI |
| Power BI | Dashboard Visualization |

---

## Project Workflow

### 1. Data Preprocessing

- Removed constant and unnecessary columns
- Handled categorical variables using encoding
- Feature scaling using StandardScaler
- Data cleaning and transformation

### 2. Exploratory Data Analysis (EDA)

Performed business-driven analysis to identify patterns related to employee attrition.

### Key Insights

- Employees working overtime are more likely to leave
- Lower salary employees show higher attrition
- Poor work-life balance increases resignation probability
- Young employees (20–25 age group) have the highest attrition rate

### 3. Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

SMOTE was applied to balance the dataset before training.

---

## Model Performance

| Model | Accuracy | Recall |
|---|---|---|
| Logistic Regression + SMOTE | 87% | 54% |
| Decision Tree + SMOTE | 77% | 44% |
| Random Forest + SMOTE | 88% | 28% |
| SVM + SMOTE | 88% | 51% |

### Best Model

Logistic Regression with SMOTE was selected as the final model due to its better recall score for identifying at-risk employees.

---

## SHAP Explainability

SHAP values were used to explain model predictions and identify the most influential features affecting attrition.

### Important Factors

- Overtime
- Monthly Income
- Work-Life Balance
- Job Level
- Total Working Years

---

## Power BI Dashboard

An interactive dashboard was developed to visualize:

- Overall Attrition Rate
- Department-wise Attrition
- Salary Analysis
- Overtime Impact
- Age Group Analysis

---

## Business Recommendations

Based on the analysis, the following strategies are recommended:

- Reduce excessive overtime workload
- Improve salary structures
- Introduce employee wellness programs
- Improve work-life balance policies
- Provide mentorship for younger employees

---

## Future Improvements

- Real-time HR system integration
- Periodic model retraining
- Employee sentiment analysis
- Deployment as a web application

---

## Conclusion

This project demonstrates how Data Analytics and Machine Learning can help organizations proactively reduce employee attrition. By identifying high-risk employees early, HR departments can take preventive measures and improve employee retention strategies.

---

## Author

Hari chandana Uggu  
B.Tech CSE (2021–2025)

---
