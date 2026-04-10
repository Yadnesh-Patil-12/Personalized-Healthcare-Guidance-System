def explain_result(result):
    if result == "Anemia":
        return "Low hemoglobin detected..."
    elif result == "Infection":
        return "High WBC count..."
    elif result == "Diabetes Risk":
        return "Maintain healthy diet..."
    else:
        return "Your report looks normal."
