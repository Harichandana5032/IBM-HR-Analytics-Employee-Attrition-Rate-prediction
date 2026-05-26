# IBM HR Analytics — Employee Attrition Prediction

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Sklearn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-green)

**Elevate Labs Data Analytics Internship Project — May 2025**

---

## Problem Statement

IBM Corporation is experiencing a **16.12% employee attrition rate**, with **Sales (20.63%)** and **HR (19.05%)** departments most affected. This leads to significant costs estimated at **6–9 months of salary per resignation** in recruitment, onboarding, and lost productivity.

**This project identifies the root causes of attrition and builds a predictive model to help HR proactively retain at-risk employees.**

---

## Key Findings

| Finding | Insight |
|---------|---------|
| **Overtime** | Employees working overtime are **4x more likely to leave** (31% vs 10%) |
| **Salary Gap** | Leavers earned **Rs.1,600/month less** than those who stayed |
| **Age Group** | Employees aged **20-25 show 36% attrition** — highest across all groups |
| **Work Life Balance** | Bad WLB group has **31% attrition rate** |

---

## Tools and Technologies

| Tool | Purpose |
|------|---------|
| **Python + Pandas** | Data cleaning and transformation |
| **Seaborn + Matplotlib** | EDA visualizations |
| **Scikit-learn** | ML models and evaluation metrics |
| **Imbalanced-learn (SMOTE)** | Class imbalance handling |
| **SHAP** | Explainable AI — model interpretation |
| **Power BI** | Interactive dashboard (2 pages) |
| **Streamlit** | Live prediction web application |

---

## Model Performance

| Model | Accuracy | Recall | Selected |
|-------|----------|--------|----------|
| **Logistic Regression + SMOTE** | **87%** | **54%** | **Yes** |
| SVM + SMOTE | 88% | 51% | No |
| Random Forest + SMOTE | 88% | 28% | No |
| Decision Tree + SMOTE | 77% | 44% | No |

**Why Recall over Accuracy?**

Missing an at-risk employee (False Negative) is far more costly than a false alarm (False Positive). Every missed prediction equals 6–9 months salary in rehiring costs. Logistic Regression with SMOTE achieved the highest Recall (54%) and was selected as the final model.

---

## Project Structure

```
HR_Attrition_Project/
├── hr_attrition_analysis.ipynb          # Main analysis notebook
├── app.py                                # Streamlit prediction app
├── model.pkl                             # Saved Logistic Regression model
├── scaler.pkl                            # Saved StandardScaler
├── WA_Fn-UseC_-HR-Employee-Attrition.csv # IBM HR Dataset
├── hr_dashboard.pbix                     # Power BI dashboard
├── HR_Attrition_Report.pdf               # 2-page project report
└── README.md                             # This file
```

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Harichandana5032/hr-attrition-prediction.git
cd hr-attrition-prediction
```

**2. Install dependencies**
```bash
pip install pandas numpy scikit-learn imbalanced-learn shap streamlit matplotlib seaborn
```

**3. Run Jupyter Notebook**
```bash
jupyter notebook hr_attrition_analysis.ipynb
```

**4. Run Streamlit App**
```bash
streamlit run app.py
```

---

## Project Workflow

```
IBM HR Dataset (1,470 employees)
         |
  Data Cleaning and Preprocessing
  (Encoding + Scaling + Feature Selection)
         |
  Exploratory Data Analysis
  (5 Business-Driven Charts + Insights)
         |
  Machine Learning Model
  (Logistic Regression + SMOTE)
         |
  SHAP Analysis
  (Feature Importance + Individual Explanations)
         |
  Power BI Dashboard + Streamlit App
  (Interactive Visualization + Live Prediction)
```

---

## HR Recommendations

Based on the analysis, the following interventions are recommended:

**1. Reduce Overtime**
Implement predictive scheduling and enforce mandatory pre-approvals for extra hours. Cross-train staff to distribute workloads evenly.

**2. Fix Salary Gaps**
Conduct quarterly compensation benchmarking and introduce structured hike and bonus policies, especially for lower salary bands.

**3. Retain Young Talent**
Introduce mentorship programs and fast-track career development paths for employees aged 20–25.

**4. Improve Work Life Balance**
Offer flexible work arrangements, enforce no-meeting days, and provide mental health support to prevent burnout.

---

## Dataset

- **Source:** IBM HR Analytics Employee Attrition Dataset — Kaggle
- **Size:** 1,470 employees x 35 features
- **Target Variable:** Attrition (Yes/No) — 16.12% positive class

---

## Author

Hari chandana Uggu
**Data Analytics Intern — Elevate Labs**
May 2025
IBM HR Analytics Project

---

## License

This project is for educational purposes as part of the Elevate Labs Data Analytics Internship Program.
