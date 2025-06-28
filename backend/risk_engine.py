def evaluate_risk(profile):
    age = profile["age"]
    income = profile["income"]
    smoker = profile["smoker"]
    diabetic = profile["diabetic"]
    bmi = profile["bmi"]

    score = 0

    if age > 50:
        score += 1
    if income == "<5L":
        score += 1
    if smoker:
        score += 2
    if diabetic:
        score += 2
    if bmi > 30:
        score += 1

    if score >= 5:
        return "High"
    elif score >= 3:
        return "Medium"
    else:
        return "Low"
