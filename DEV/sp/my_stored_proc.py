def process_score(score: int) -> str:
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    elif score >= 89:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    else:
        return "Poor"
