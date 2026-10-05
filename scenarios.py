# EMT-AI Checkpoint 2
# Fictional training scenarios used to test the prototype.

SCENARIOS = [
    {
        "id": 1,
        "title": "Unconscious Patient",
        "description": (
            "A 45-year-old patient is lying on the floor and is "
            "unresponsive. The patient is breathing."
        ),
        "expected_priority": "HIGH"
    },
    {
        "id": 2,
        "title": "Chest Pain",
        "description": (
            "A 62-year-old patient reports severe chest pain, "
            "shortness of breath, and sweating."
        ),
        "expected_priority": "HIGH"
    },
    {
        "id": 3,
        "title": "Minor Cut",
        "description": (
            "A 20-year-old patient has a small cut on the hand. "
            "Bleeding is minor and the patient is alert."
        ),
        "expected_priority": "LOW"
    },
    {
        "id": 4,
        "title": "Severe Bleeding",
        "description": (
            "A patient has a deep leg injury with severe bleeding "
            "after an accident."
        ),
        "expected_priority": "HIGH"
    },
    {
        "id": 5,
        "title": "Possible Broken Arm",
        "description": (
            "A patient fell while playing basketball and has severe "
            "arm pain and swelling. The patient is alert and breathing normally."
        ),
        "expected_priority": "MEDIUM"
    },
    {
        "id": 6,
        "title": "Difficulty Breathing",
        "description": (
            "A 35-year-old patient is having shortness of breath "
            "and difficulty speaking in full sentences."
        ),
        "expected_priority": "HIGH"
    },
    {
        "id": 7,
        "title": "Ankle Injury",
        "description": (
            "A patient twisted an ankle while running. There is swelling "
            "and pain, but the patient is alert and breathing normally."
        ),
        "expected_priority": "MEDIUM"
    },
    {
        "id": 8,
        "title": "Headache",
        "description": (
            "A patient reports a mild headache after a long day. "
            "The patient is alert and breathing normally."
        ),
        "expected_priority": "LOW"
    },
    {
        "id": 9,
        "title": "Possible Fracture",
        "description": (
            "A patient fell down several stairs and may have a fracture "
            "in the lower leg. The patient is alert."
        ),
        "expected_priority": "MEDIUM"
    },
    {
        "id": 10,
        "title": "Weak Case - Breathing Emergency",
        "description": (
            "A patient says they cannot catch their breath and appears "
            "very distressed."
        ),
        "expected_priority": "HIGH"
    }
]