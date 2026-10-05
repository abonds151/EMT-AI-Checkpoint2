**Antonio Bonds II**
**COMP 365**
**EMT-AI Checkpoint 2 README**
**10/04/2026**

# EMT-AI: Intelligent Emergency Response Training Assistant

## Checkpoint 2 Prototype

EMT-AI is a prototype training assistant designed to analyze fictional emergency scenarios and provide a suggested priority level and training feedback.

The purpose of this project is to explore whether a simple intelligent training assistant can identify important warning signs in EMT-style scenarios more accurately than a basic rule-based baseline.

This project is for educational and training purposes only. It is not intended to provide real medical advice, diagnosis, treatment, or emergency instructions.

## How the Prototype Works

The program reads a fictional emergency scenario and searches for warning signs.
The current prototype classifies scenarios into three priority levels:

- HIGH
- MEDIUM
- LOW

It also provides basic training feedback. With further research I will be able to use actual medical terms. For the basic prototype, it will do. Future ideas will give this prototype the edge I think it needs.

## Files

- `main.py` - Runs the EMT-AI prototype.
- `emt_ai.py` - Contains the EMT-AI analysis logic.
- `baseline.py` - Contains the simple baseline comparison method.
- `scenarios.py` - Contains the fictional test scenarios.
- `test_systems.py` - Tests EMT-AI and the baseline on the same scenarios.
- `results.txt` - Contains the current Checkpoint 2 test results.

## Running EMT-AI
//AI assisted with this section, I had troubles making it run but in the end the prototype works.
Run:

```bash
python3 main.py
