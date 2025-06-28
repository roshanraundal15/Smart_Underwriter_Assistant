import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini model
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_explanation(profile, risk_level):
    age = profile["age"]
    bmi = profile["bmi"]
    smoker = profile["smoker"]
    diabetic = profile["diabetic"]
    income = profile["income"]
    diabetic_details = profile.get("diabetic_details", {})
    smoker_details = profile.get("smoker_details", {})

    # Highlighted risk indicators
    age_text = f"**AGE: {age} (SENIOR)**" if age >= 60 else f"**AGE:** {age}"
    bmi_text = f"**BMI: {bmi} (HIGH)**" if bmi > 30 else f"**BMI:** {bmi}"
    smoker_text = "**SMOKER**" if smoker else "**Non-Smoker**"
    diabetic_text = "**DIABETIC**" if diabetic else "**Non-Diabetic**"
    income_text = "**LOW INCOME**" if income == "<5L" else f"**Income:** {income}"

    # Additional diabetic info
    diabetic_additional_info = ""
    if diabetic and diabetic_details:
        diabetic_additional_info = f"""
- **Type of Diabetes**: {diabetic_details.get('type', 'N/A')}
- **Years Since Diagnosis**: {diabetic_details.get('years_since_diagnosis', 'N/A')}
- **On Medication**: {diabetic_details.get('on_medication', 'N/A')}
- **Controlled**: {diabetic_details.get('controlled', 'N/A')}
"""

    # Additional smoker info
    smoker_additional_info = ""
    if smoker and smoker_details:
        smoker_additional_info = f"""
- **Type of Smoking**: {smoker_details.get('type', 'N/A')}
- **Frequency**: {smoker_details.get('frequency', 'N/A')}
- **Years Smoking**: {smoker_details.get('years_smoking', 'N/A')}
- **Trying to Quit**: {smoker_details.get('trying_to_quit', 'N/A')}
"""

    prompt = f"""
You are an expert insurance underwriter assistant.

Explain in exactly **10 professional bullet points** why the applicant's risk level is **{risk_level}**.

Instructions:
- Use **bold** for keywords like AGE, BMI, SMOKER, DIABETIC, etc.
- Be formal, clear, and to the point.
- Avoid repeating the risk level phrase inside the explanation.

### Profile Summary:
- {age_text}
- {bmi_text}
- {smoker_text}
- {diabetic_text}
- {income_text}
{diabetic_additional_info}
{smoker_additional_info}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"
