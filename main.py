# EMT-AI Checkpoint 2
# Main program

from scenarios import SCENARIOS
from emt_ai import analyze_scenario


def main():

    print("=" * 55)
    print("EMT-AI: Emergency Response Training Assistant")
    print("Checkpoint 2 Prototype")
    print("=" * 55)

    print("\nFOR EDUCATIONAL AND TRAINING PURPOSES ONLY")
    print("This program does not provide real medical advice.\n")

    correct = 0

    for scenario in SCENARIOS:

        print("-" * 55)
        print(f"Scenario {scenario['id']}: {scenario['title']}")
        print()
        print(scenario["description"])

        result = analyze_scenario(scenario["description"])

        print()
        print(f"EMT-AI Priority: {result['priority']}")
        print(f"Expected Priority: {scenario['expected_priority']}")
        print(f"Training Feedback: {result['feedback']}")

        if result["priority"] == scenario["expected_priority"]:
            print("Test Result: CORRECT")
            correct += 1
        else:
            print("Test Result: INCORRECT")

        print()

    total = len(SCENARIOS)
    accuracy = (correct / total) * 100

    print("=" * 55)
    print("TEST SUMMARY")
    print("=" * 55)

    print(f"Scenarios Tested: {total}")
    print(f"Correct Results: {correct}")
    print(f"Incorrect Results: {total - correct}")
    print(f"Accuracy: {accuracy:.1f}%")


if __name__ == "__main__":
    main()