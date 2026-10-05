# EMT-AI Checkpoint 2
# Comparison test between EMT-AI and the baseline.

from scenarios import SCENARIOS
from emt_ai import analyze_scenario
from baseline import baseline_analyze


def run_tests():

    emt_correct = 0
    baseline_correct = 0

    print("=" * 75)
    print("EMT-AI CHECKPOINT 2 - COMPARISON TEST")
    print("=" * 75)

    for scenario in SCENARIOS:

        expected = scenario["expected_priority"]

        emt_result = analyze_scenario(
            scenario["description"]
        )["priority"]

        baseline_result = baseline_analyze(
            scenario["description"]
        )

        if emt_result == expected:
            emt_correct += 1
            emt_status = "CORRECT"
        else:
            emt_status = "INCORRECT"

        if baseline_result == expected:
            baseline_correct += 1
            baseline_status = "CORRECT"
        else:
            baseline_status = "INCORRECT"

        print()
        print(f"Scenario {scenario['id']}: {scenario['title']}")
        print(f"Expected: {expected}")
        print(f"EMT-AI:   {emt_result} ({emt_status})")
        print(f"Baseline: {baseline_result} ({baseline_status})")

    total = len(SCENARIOS)

    emt_accuracy = (emt_correct / total) * 100
    baseline_accuracy = (baseline_correct / total) * 100

    print()
    print("=" * 75)
    print("FINAL COMPARISON")
    print("=" * 75)

    print(f"Total Test Cases: {total}")
    print()

    print(
        f"EMT-AI:   {emt_correct}/{total} correct "
        f"({emt_accuracy:.1f}%)"
    )

    print(
        f"Baseline: {baseline_correct}/{total} correct "
        f"({baseline_accuracy:.1f}%)"
    )


if __name__ == "__main__":
    run_tests()