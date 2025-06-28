def generate_recommendations(profile, risk_level):
    recommendations = []

    age = profile.get("age", 0)
    bmi = profile.get("bmi", 0)
    smoker = profile.get("smoker", False)
    diabetic = profile.get("diabetic", False)
    income = profile.get("income", "")


    # Risk-level based core recommendations
    if risk_level == "High":
        recommendations += [
            "🔴 Consider comprehensive health insurance with a critical illness rider.",
            "💡 Choose higher coverage with lifetime renewability.",
            "🩺 Schedule frequent health check-ups (every 6 months).",
            "⚖️ Consult a dietician and fitness coach to manage BMI and reduce comorbidities.",
            "💊 If diabetic, ensure your medication is regular and blood sugar is monitored.",
        ]
    elif risk_level == "Medium":
        recommendations += [
            "🟡 Opt for a term insurance plan with moderate coverage and annual reviews.",
            "🧘 Focus on a proactive lifestyle – include walking, yoga, or cardio weekly.",
            "📊 Track BMI and blood sugar annually; adjust lifestyle accordingly.",
            "🧪 Consider affordable preventive healthcare screening plans.",
            "💬 Speak to an insurance advisor for policy bundling strategies.",
        ]
    else:  # Low Risk
        recommendations += [
            "🟢 Maintain your healthy habits and monitor health indicators yearly.",
            "✅ Lock in low premiums early with a long-term term insurance policy.",
            "📋 Reassess insurance coverage every 2–3 years as life circumstances change.",
            "🛡️ Explore low-cost add-ons like accidental cover or top-ups.",
            "📈 Consider investing in a health savings plan or wellness benefits.",
        ]

    # Personalized adjustments
    if diabetic:
        recommendations.append("🩸 Manage **DIABETES** with regular HbA1c testing and proper medication.")
    if smoker:
        recommendations.append("🚭 Join a smoking cessation program and reduce tobacco usage.")
    if bmi > 30:
        recommendations.append("📉 Focus on reducing **BMI** through diet, portion control, and movement.")
    if age >= 60:
        recommendations.append("👴 Consider senior-citizen-focused insurance plans with tailored benefits.")
    if income == "<5L":
        recommendations.append("💰 Explore government-subsidized or affordable health insurance schemes.")

    return recommendations
