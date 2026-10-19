
# EMT-AI: Three-Level Comparison Baseline
# Educational use with fictional scenarios only.

def three_level_analyze(description):
    text = description.lower()

    high_terms = [
        "unconscious",
        "unresponsive",
        "chest pain",
        "severe bleeding",
        "not breathing"
    ]

    medium_terms = [
        "broken",
        "fracture",
        "swelling",
        "arm pain"
    ]

    for term in high_terms:
        if term in text:
            return "HIGH"

    for term in medium_terms:
        if term in text:
            return "MEDIUM"

    return "LOW"
