# app1.py (Enhanced Recommendation Engine)
import streamlit as st
from utils.recommendation_engine import generate_recommendations

st.set_page_config(page_title="Personalized Risk Advice", layout="centered")
st.title("💡 Personalized Recommendation Engine")

st.markdown("Provide your health profile below to receive intelligent lifestyle and wellness suggestions tailored to reduce your insurance risk.")

# Input Section
age = st.slider("👤 Age", 18, 100, 30)
bmi = st.slider("📏 BMI", 10, 45, 24)
income = st.selectbox("💰 Annual Income (₹ Lakhs)", [
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
    profile["diabetic_details"] = {
        "type": st.selectbox("Type of Diabetes", ["Type 1", "Type 2", "Gestational"]),
        "years_since_diagnosis": st.slider("Years since diagnosis", 0, 50, 5),
        "on_medication": st.radio("On Medication?", ["Yes", "No"]),
        "controlled": st.radio("Controlled?", ["Yes", "No"])
    }

if smoker:
    profile["smoker_details"] = {
        "type": st.selectbox("Type of Smoking", ["Cigarettes", "Cigars", "Vape", "Hookah", "Other"]),
        "frequency": st.selectbox("Frequency", ["Occasional", "Daily", "Heavy"]),
        "years_smoking": st.slider("Years of Smoking", 0, 50, 5),
        "trying_to_quit": st.radio("Trying to quit?", ["Yes", "No"])
    }

# Show Recommendations
if st.button("🔍 Get My Recommendations"):
    st.markdown("### 🧠 Personalized Suggestions")

    recommendations = generate_recommendations(profile, risk_level="medium")

    # Pad to ensure minimum of 10
    generic_advice = [
        "Engage in at least 30 minutes of moderate physical activity daily to maintain a healthy weight.",
        "Include high-fiber foods like vegetables, legumes, and whole grains in your diet.",
        "Reduce intake of processed foods, sugary beverages, and trans fats to manage cardiovascular risk.",
        "Stay well hydrated and limit caffeine and alcohol consumption.",
        "Regularly monitor your blood pressure, cholesterol, and blood sugar levels.",
        "Build a consistent sleep schedule and aim for 7–8 hours of quality rest each night.",
        "Practice stress management techniques such as deep breathing, meditation, or mindful walking.",
        "Consider consulting a certified nutritionist for a diet plan tailored to your needs.",
        "Stay compliant with prescribed medications and attend all follow-up medical checkups.",
        "Join a support group or health-focused community to stay motivated and accountable."
    ]
    
    # Top-up if fewer than 10
    while len(recommendations) < 10:
        recommendations.append(generic_advice[len(recommendations) % len(generic_advice)])

    for rec in recommendations[:10]:
        st.markdown(f"- {rec}")

    st.success("✅ These recommendations are designed to improve your health profile and reduce your risk exposure.")
