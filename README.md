**Antonio Bonds II**
**COMP 365**
**EMT-AI Checkpoint 2 README**
**10/04/2026**


# EMT-AI: Emergency Response Training Assistant

## Project Overview

EMT-AI is a rule-based emergency response training
assistant designed for fictional EMT scenarios.

The program reads a description of a patient's
condition and assigns a training priority:

- HIGH: Potentially serious warning signs
- MEDIUM: Conditions requiring further assessment
- LOW: Minor conditions without recognized warning signs

The program also provides basic training feedback.

## Project Objective

The goal is to develop and evaluate a computer-based
system that helps EMT trainees practice identifying
warning signs in fictional emergency scenarios.

Research Question:

Can EMT-AI classify fictional emergency scenarios
more accurately than simple rule-based baselines?

## How the System Works

1. The user provides a fictional patient description.
2. EMT-AI converts the description to lowercase.
3. It searches for predefined warning phrases.
4. It assigns HIGH, MEDIUM, or LOW priority.
5. It provides training feedback.

EMT-AI currently uses predefined rules and keywords.
It does not use a trained machine-learning model.

## Project Files

- emt_ai.py: Main EMT-AI classification system
- baseline.py: Original comparison system
- three_level_baseline.py: Improved comparison system
- scenarios.py: Development scenarios
- independent_scenarios.py: Additional test scenarios
- test_systems.py: Development testing
- independent_test.py: Additional scenario testing
- results_table.py: Comparison table and CSV export
- comparison_results.csv: Development comparison data
- results.txt: Experimental results and limitations
- main.py: Main program entry point

## Experimental Results

### Development Test

| System | Correct | Accuracy |
|---|---|---|
| Original Baseline | 5/10 | 50% |
| Three-Level Baseline | 8/10 | 80% |
| EMT-AI | 10/10 | 100% |

### Additional Scenario Test

| System | Correct | Accuracy |
|---|---|---|
| Original Baseline | 5/10 | 50% |
| Three-Level Baseline | 7/10 | 70% |
| EMT-AI | 10/10 | 100% |

## Results Discussion

EMT-AI achieved the highest accuracy on both sets
of fictional scenarios.

The original baseline achieved 50% accuracy on
both tests.

The three-level baseline achieved 80% accuracy
on the development test and 70% accuracy on
the additional test.

These results suggest that the more detailed
keyword rules in EMT-AI worked better on the
selected scenarios.

## Limitations

The project used only 20 fictional scenarios
across two tests.

The additional scenarios included wording similar
to the development scenarios.

The expected priority labels have not been
independently validated by EMT instructors.

The project does not demonstrate machine-learning
performance or clinical reliability.

Future work could include more diverse scenarios,
expert-reviewed labels, testing with paraphrased
descriptions, and comparison with a trained
machine-learning classifier.

## Running the Project

Run the development tests:

python3 test_systems.py

Run the additional tests:

python3 independent_test.py

Generate the comparison table:

python3 results_table.py

## Safety Disclaimer

EMT-AI is an educational prototype for fictional
training scenarios only.

It is not intended for real patient triage,
emergency response decisions, diagnosis,
or medical advice.

All real emergency decisions must be made by
qualified professionals following approved protocols.
