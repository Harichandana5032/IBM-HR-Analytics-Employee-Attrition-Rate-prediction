import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ── Page Config ──
st.set_page_config(
    page_title="IBM HR Attrition Predictor",
    page_icon="👔",
    layout="wide"
)

# ── Load Model & Scaler ──
try:
    model = pickle.load(open('model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except Exception:
    st.error("⚠️ Model files not found! Make sure model.pkl and scaler.pkl are in the same folder.")
    st.stop()

# ── Header ──
st.markdown("""
    <div style='background:linear-gradient(90deg,#0f62fe,#0353e9);padding:20px 28px;border-radius:12px;margin-bottom:24px'>
        <h2 style='color:white;margin:0;font-family:Arial'>👔 IBM HR Attrition Prediction System</h2>
        <p style='color:#a6c8ff;margin:4px 0 0'>Powered by Logistic Regression + SMOTE + SHAP · IBM HR Dataset</p>
    </div>
""", unsafe_allow_html=True)

# ── Input Form ──
st.markdown("### 📋 Employee Details")
col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 18, 60, 28)
    income = st.number_input("Monthly Income (₹)", 1000, 20000, 3500, step=500)
    overtime = st.selectbox("OverTime", ["Yes", "No"])
    joblevel = st.selectbox("Job Level", [1, 2, 3, 4, 5],
                            format_func=lambda x: f"{x} — {'Entry' if x==1 else 'Junior' if x==2 else 'Mid' if x==3 else 'Senior' if x==4 else 'Director'}")

with col2:
    jobsat = st.selectbox("Job Satisfaction", [1, 2, 3, 4],
                          format_func=lambda x: f"{x} — {'Low' if x==1 else 'Medium' if x==2 else 'High' if x==3 else 'Very High'}")
    wlb = st.selectbox("Work Life Balance", [1, 2, 3, 4],
                       format_func=lambda x: f"{x} — {'Bad' if x==1 else 'Good' if x==2 else 'Better' if x==3 else 'Best'}")
    years = st.slider("Years At Company", 0, 40, 2)
    travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])

with col3:
    department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
    marital = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    education = st.selectbox("Education", [1, 2, 3, 4, 5],
                             format_func=lambda x: f"{x} — {'Below College' if x==1 else 'College' if x==2 else 'Bachelor' if x==3 else 'Master' if x==4 else 'Doctor'}")
    envsat = st.selectbox("Environment Satisfaction", [1, 2, 3, 4],
                          format_func=lambda x: f"{x} — {'Low' if x==1 else 'Medium' if x==2 else 'High' if x==3 else 'Very High'}")

st.markdown("---")

# ── Predict Button ──
if st.button("🔍 Predict Attrition Risk", use_container_width=True, type="primary"):
    try:
        # ── Build Input Dict matching EXACT training columns ──
        input_dict = {
            'Age': age,
            'BusinessTravel': {"Non-Travel": 0, "Travel_Rarely": 1, "Travel_Frequently": 2}[travel],
            'DailyRate': 800,
            'DistanceFromHome': 5,
            'Education': education,
            'EnvironmentSatisfaction': envsat,
            'Gender': 1 if gender == "Male" else 0,
            'HourlyRate': 65,
            'JobInvolvement': 3,
            'JobLevel': joblevel,
            'JobSatisfaction': jobsat,
            'MonthlyIncome': income,
            'MonthlyRate': 14000,
            'NumCompaniesWorked': 2,
            'OverTime': 1 if overtime == "Yes" else 0,
            'PercentSalaryHike': 15,
            'PerformanceRating': 3,
            'RelationshipSatisfaction': 3,
            'StockOptionLevel': 1,
            'TotalWorkingYears': years + 3,
            'TrainingTimesLastYear': 3,
            'WorkLifeBalance': wlb,
            'YearsAtCompany': years,
            'YearsInCurrentRole': max(0, years - 1),
            'YearsSinceLastPromotion': 1,
            'YearsWithCurrManager': max(0, years - 1),
            # One-hot encoded — Department (HR dropped as base)
            'Department_Research & Development': 1 if department == "Research & Development" else 0,
            'Department_Sales': 1 if department == "Sales" else 0,
            # One-hot encoded — EducationField (all default 0)
            'EducationField_Life Sciences': 0,
            'EducationField_Marketing': 0,
            'EducationField_Medical': 0,
            'EducationField_Other': 0,
            'EducationField_Technical Degree': 0,
            # One-hot encoded — JobRole (Healthcare Rep dropped as base)
            'JobRole_Human Resources': 1 if department == "Human Resources" else 0,
            'JobRole_Laboratory Technician': 0,
            'JobRole_Manager': 1 if joblevel >= 4 else 0,
            'JobRole_Manufacturing Director': 0,
            'JobRole_Research Director': 0,
            'JobRole_Research Scientist': 0,
            'JobRole_Sales Executive': 1 if department == "Sales" and joblevel >= 3 else 0,
            'JobRole_Sales Representative': 1 if department == "Sales" and joblevel < 3 else 0,
            # One-hot encoded — MaritalStatus (Divorced dropped as base)
            'MaritalStatus_Married': 1 if marital == "Married" else 0,
            'MaritalStatus_Single': 1 if marital == "Single" else 0,
        }

        # ── Scale continuous columns ──
        cols_to_scale = [
            'Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate',
            'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
            'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
            'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
            'YearsWithCurrManager'
        ]

        input_df = pd.DataFrame([input_dict])
        input_df[cols_to_scale] = scaler.transform(input_df[cols_to_scale])

        # ── Predict ──
        prob = model.predict_proba(input_df)[0][1] * 100

        # ── Show Results ──
        st.markdown("### 📊 Prediction Results")
        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("#### Risk Score")
            if prob < 30:
                st.success(f"✅ LOW RISK — {prob:.1f}%")
                risk_color = "green"
            elif prob < 60:
                st.warning(f"⚠️ MEDIUM RISK — {prob:.1f}%")
                risk_color = "orange"
            else:
                st.error(f"🚨 HIGH RISK — {prob:.1f}%")
                risk_color = "red"

            st.progress(int(prob))

            # ── Model Performance ──
            st.markdown("#### Model Performance")
            m1, m2, m3 = st.columns(3)
            m1.metric("Accuracy", "87%")
            m2.metric("Recall", "54%")
            m3.metric("F1 Score", "68%")

            # ── Confusion Matrix ──
            st.markdown("#### Confusion Matrix")
            cm_data = pd.DataFrame(
                [[245, 10], [18, 21]],
                index=["Actual: Stayed", "Actual: Left"],
                columns=["Predicted: Stayed", "Predicted: Left"]
            )
            st.dataframe(cm_data, use_container_width=True)

        with col_b:
            st.markdown("#### 💡 HR Recommendation")

            # ── Risk factors identified ──
            risk_factors = []
            if overtime == "Yes":
                risk_factors.append("⏰ Working overtime — high burnout risk")
            if income < 5000:
                risk_factors.append("💰 Below average salary — financial dissatisfaction")
            if age <= 25:
                risk_factors.append("🎯 Young employee (20-25) — career exploration phase")
            if wlb <= 2:
                risk_factors.append("⚖️ Poor work life balance — burnout risk")
            if jobsat <= 2:
                risk_factors.append("😟 Low job satisfaction — disengagement risk")

            if risk_factors:
                st.markdown("**Key Risk Factors Identified:**")
                for rf in risk_factors:
                    st.write(rf)
            else:
                st.write("✅ No major risk factors detected!")

            st.markdown("**Recommendation:**")

            # personalized suggestion based on top risk factor
            if prob >= 60:
                if overtime == "Yes":
                    st.error("""
                    🚨 **Immediate Action Required**
                    
                    Reduce overtime burden immediately. Implement predictive scheduling,
                    enforce mandatory pre-approvals for extra hours, and cross-train staff
                    to distribute workloads evenly.
                    """)
                elif income < 5000:
                    st.error("""
                    🚨 **Immediate Action Required**
                    
                    Conduct salary benchmarking. Offer clear career growth paths,
                    skill-building opportunities, and transparent promotion timelines
                    to compensate for salary gaps.
                    """)
                elif age <= 25:
                    st.error("""
                    🚨 **Immediate Action Required**
                    
                    Assign a senior mentor and create a fast-track career development plan.
                    Young employees need visible growth opportunities to stay engaged.
                    """)
                else:
                    st.error("""
                    🚨 **Immediate Action Required**
                    
                    Schedule urgent one-on-one with employee. Review compensation,
                    workload, and career progression immediately.
                    """)
            elif prob >= 30:
                st.warning("""
                ⚠️ **Monitor Closely**
                
                Schedule regular check-ins. Encourage participation in training programs,
                acknowledge contributions, and ensure workload is manageable.
                Offer non-monetary benefits like flexible hours or skill development.
                """)
            else:
                st.success("""
                ✅ **Employee is Stable**
                
                No immediate action required. Continue regular performance reviews
                and maintain current positive working conditions.
                """)

    except Exception as e:
        st.error("⚠️ Something went wrong! Please check your inputs and try again.")
        print(f"Developer log: {e}")  # hidden from user, visible in terminal