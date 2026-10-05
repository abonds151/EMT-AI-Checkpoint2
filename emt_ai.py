# EMT-AI Checkpoint 2
# Prototype emergency training assistant.
#
# IMPORTANT:
# This program is for educational/testing purposes only.
# It is not intended to provide real medical advice.


def analyze_scenario(description):
    """
    Analyze a fictional EMT training scenario and return
    a priority level and training feedback.
    """

    text = description.lower()

    high_priority_terms = [
        "unresponsive",
        "unconscious",
        "severe bleeding",
        "chest pain",
        "shortness of breath",
        "not breathing"
    ]

    medium_priority_terms = [
        "severe arm pain",
        "swelling",
        "broken",
        "fracture",
        "moderate bleeding"
    ]

    # Check for high-priority warning signs.
    for term in high_priority_terms:
        if term in text:
            return {
                "priority": "HIGH",
                "feedback": (
                    "The scenario contains a potentially serious warning sign. "
                    "The trainee should perform an immediate primary assessment "
                    "and follow the appropriate training protocol."
                )
            }

    # Check for medium-priority warning signs.
    for term in medium_priority_terms:
        if term in text:
            return {
                "priority": "MEDIUM",
                "feedback": (
                    "The patient appears stable, but the injury may require "
                    "additional assessment and treatment."
                )
            }

    # If no major warning signs are detected.
    return {
        "priority": "LOW",
        "feedback": (
            "No high-priority warning signs were detected by the prototype. "
            "Continue assessing the patient and follow the appropriate "
            "training protocol."
        )
    }