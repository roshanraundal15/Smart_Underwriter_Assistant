from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
from io import BytesIO
import textwrap

def generate_underwriting_pdf(profile, risk, explanation, recommendations):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    margin = 50
    line_height = 15
    y = height - margin

    def check_page(lines=1):
        nonlocal y
        if y - (lines * line_height) < 60:
            add_footer()
            c.showPage()
            y = height - margin

    def add_footer():
        c.setFont("Helvetica-Oblique", 9)
        now = datetime.now().strftime("%d %b %Y, %I:%M %p")
        c.drawString(margin, 30, f"Generated on: {now}")
        c.drawRightString(width - margin, 30, "🔒 Powered by Smart Underwriting AI Agent")

    def draw_bold_label(label):
        nonlocal y
        check_page()
        c.setFont("Helvetica-Bold", 13)
        c.drawString(margin, y, label)
        y -= 20

    def draw_key_values(data_dict):
        nonlocal y
        c.setFont("Helvetica", 11)
        for k, v in data_dict.items():
            check_page()
            c.drawString(margin + 20, y, f"{k.capitalize()}: {v}")
            y -= line_height

    def draw_text_block(text, spacing_above=5, spacing_below=5):
        nonlocal y
        y -= spacing_above
        lines = textwrap.wrap(text, width=90)
        c.setFont("Helvetica", 11)
        for line in lines:
            check_page()
            c.drawString(margin + 20, y, line.strip())
            y -= line_height
        y -= spacing_below

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, y, "📄 Smart Underwriting Risk Report")
    y -= 30

    # Risk Level
    draw_bold_label("■ Risk Level:")
    c.setFont("Helvetica", 11)
    c.drawString(margin + 20, y, f"{risk.upper()}")
    y -= 25

    # Applicant Profile
    draw_bold_label("■ Applicant Profile:")
    draw_key_values(profile)

    # Highlighted Risk Factors
    draw_bold_label("■ Highlighted Risk Factors:")
    risk_factors = []
    if profile.get("smoker"): risk_factors.append("🚬 Smoker")
    if profile.get("diabetic"): risk_factors.append("🩺 Diabetic")
    if profile.get("bmi", 0) > 30: risk_factors.append("⚠️ High BMI")
    if profile.get("age", 0) >= 60: risk_factors.append("👴 Senior Age")
    if profile.get("income") == "<5L": risk_factors.append("💰 Low Income")
    if not risk_factors: risk_factors.append("None")
    for rf in risk_factors:
        draw_text_block(f"- {rf}", spacing_above=2, spacing_below=2)

    # Explanation Section
    draw_bold_label("■ Explanation:")
    for line in explanation.strip().split("\n"):
        draw_text_block(line, spacing_above=0, spacing_below=2)

    # Recommendation Section
    draw_bold_label("■ Recommendations:")
    for rec in recommendations:
        draw_text_block(f"- {rec}", spacing_above=2, spacing_below=2)

    # Final Footer
    add_footer()
    c.save()
    buffer.seek(0)
    return buffer
