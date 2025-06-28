# app.py (main risk assessment app)
import streamlit as st
from risk_engine import evaluate_risk
from llm_explainer import generate_explanation
from utils.pdf_generator import generate_underwriting_pdf
from utils.trend_engine import generate_risk_trend_data, risk_to_score

import base64
import os
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Title and intro
st.title("🧠 Risk Profiling Engine")
st.markdown("##### 📋 Fill out the profile below to assess insurance risk level.")

# Layout
left, right = st.columns([3, 7])

with left:
    st.markdown("### 🔧 Profile Input")
    age = st.slider("👤 Age", 18, 100, 30)
    bmi = st.slider("📏 BMI", 10, 45, 24)
    income = st.selectbox("💰 Annual Income (in ₹ Lakhs)", [
        "<2L", "2L–3L", "3L–4L", "4L–6L", "6L–8L", "8L–10L", "10L–13L", "13L–19L", ">20L"
    ])
    smoker = st.checkbox("🚬 Smoker")
    diabetic = st.checkbox("🩺 Diabetic")

    profile = {
        "age": age,
        "income": income,
        "smoker": smoker,
        "diabetic": diabetic,
        "bmi": bmi
    }

    if diabetic:
        st.markdown("#### 🔍 Diabetes Details")
        diabetic_details = {
            "type": st.selectbox("Type of Diabetes", ["Type 1", "Type 2", "Gestational"]),
            "years_since_diagnosis": st.slider("Years since diagnosis", 0, 50, 5),
            "on_medication": st.radio("Currently on medication?", ["Yes", "No"]),
            "controlled": st.radio("Is it well controlled?", ["Yes", "No"])
        }
        profile["diabetic_details"] = diabetic_details

    if smoker:
        st.markdown("#### 🚬 Smoking Details")
        smoker_details = {
            "type": st.selectbox("Type of Smoking", ["Cigarettes", "Cigars", "Vape", "Hookah", "Other"]),
            "frequency": st.selectbox("Frequency", ["Occasional", "Daily", "Heavy"]),
            "years_smoking": st.slider("Years of Smoking", 0, 50, 5),
            "trying_to_quit": st.radio("Currently trying to quit?", ["Yes", "No"])
        }
        profile["smoker_details"] = smoker_details

    st.markdown("### 🛡️ Validation Check")
    valid = True
    error_messages = []

    if smoker and "smoker_details" in profile:
        max_smoke_years = max(age - 10, 0)
        if profile["smoker_details"]["years_smoking"] > max_smoke_years:
            valid = False
            error_messages.append(f"🚫 Smoking duration cannot exceed {max_smoke_years} years based on age {age}.")

    if diabetic and "diabetic_details" in profile:
        max_diabetes_years = max(age - 1, 0)
        if profile["diabetic_details"]["years_since_diagnosis"] > max_diabetes_years:
            valid = False
            error_messages.append(f"🚫 Diabetes duration cannot exceed {max_diabetes_years} years based on age {age}.")

    evaluate_button = st.button("🚀 Evaluate Risk")

with right:
    if evaluate_button:
        if not valid:
            for msg in error_messages:
                st.error(msg)
        else:
            with st.spinner("Analyzing profile..."):
                risk = evaluate_risk(profile)
                explanation = generate_explanation(profile, risk)
                trend_data = generate_risk_trend_data(profile)  # 5-year risk trend

            st.markdown(f"## 🔍 Risk Level: `{risk}`")

            with st.expander("📑 Explanation of Risk Classification"):
                st.markdown(explanation)

            # 📈 5-Year Risk Trend Chart
            st.markdown("### 📈 Risk Trend Over 5 Years")
            fig, ax = plt.subplots()
            years = list(trend_data.keys())
            scores = [risk_to_score(r) for r in trend_data.values()]
            ax.plot(years, scores, marker='o', linestyle='-', color='orange')
            ax.set_xticks(years)
            ax.set_yticks([1, 2, 3])
            ax.set_yticklabels(["Low", "Medium", "High"])
            ax.set_ylabel("Risk Level")
            ax.set_title("Applicant's Risk Trend Over 5 Years")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)

            # 💰 Premium Affordability Estimator
            st.markdown("### 💰 Premium Affordability Estimator")

            income_map = {
                "<2L": 1.5,
                "2L–3L": 2.5,
                "3L–4L": 3.5,
                "4L–6L": 5.0,
                "6L–8L": 7.0,
                "8L–10L": 9.0,
                "10L–13L": 11.5,
                "13L–19L": 16.0,
                ">20L": 22.0,
            }

            annual_income_lakhs = income_map[income]
            estimated_premium = round((annual_income_lakhs * 100000 * 0.03) / 12)
            min_premium = int(estimated_premium * 0.7)
            max_premium = int(estimated_premium * 1.3)

            st.markdown(f"**Estimated Monthly Premium:** ₹{estimated_premium}")
            fig2, ax2 = plt.subplots(figsize=(6, 2))
            ax2.barh(["Premium Range"], [max_premium], color="#e0e0e0", edgecolor="black")
            ax2.barh(["Premium Range"], [estimated_premium], color="#4CAF50")
            ax2.axvline(min_premium, color="red", linestyle="--", label=f"Min ₹{min_premium}")
            ax2.axvline(max_premium, color="blue", linestyle="--", label=f"Max ₹{max_premium}")
            ax2.axvline(estimated_premium, color="green", linestyle="-", label=f"Est. ₹{estimated_premium}")
            ax2.set_xlim(0, max_premium + 3000)
            ax2.set_xlabel("Monthly Premium (₹)")
            ax2.legend(loc="upper right")
            ax2.set_yticks([])
            st.pyplot(fig2)

            # 📄 PDF Download
            st.markdown("### 📄 Download Underwriting Report")
            pdf_bytes = generate_underwriting_pdf(profile, risk, explanation, [])
            b64_pdf = base64.b64encode(pdf_bytes.read()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="Smart_Underwriting_Report.pdf">📥 Download PDF</a>'
            st.markdown(href, unsafe_allow_html=True)
