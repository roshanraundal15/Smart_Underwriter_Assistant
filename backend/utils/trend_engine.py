import random

def generate_risk_trend_data(profile):
    """
    Simulate the applicant's historical risk classification for the last 5 years.
    This mock function randomly adjusts the current risk up/down to show a trend.
    """
    current_risk = evaluate_risk(profile)
    years = [2020, 2021, 2022, 2023, 2024]
    risk_levels = ["Low", "Medium", "High"]
    base_index = risk_levels.index(current_risk)
    
    trend = {}
    for year in years:
        delta = random.choice([-1, 0, 1])
        new_index = min(max(base_index + delta, 0), 2)
        trend[year] = risk_levels[new_index]
    return trend

def risk_to_score(risk):
    return {"Low": 1, "Medium": 2, "High": 3}[risk]

# Local import to avoid circular dependency
from risk_engine import evaluate_risk
