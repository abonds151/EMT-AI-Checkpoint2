# EMT-AI Checkpoint 2
# Simple baseline used for comparison with EMT-AI.


def baseline_analyze(description):
    """
    Basic comparison method.

    The baseline only recognizes a few obvious emergency words.
    Anything else is classified as LOW priority.
    """

    text = description.lower()

    emergency_terms = [
        "unconscious",
        "unresponsive",
        "chest pain",
        "severe bleeding"
    ]

    for term in emergency_terms:
        if term in text:
            return "HIGH"

    return "LOW"