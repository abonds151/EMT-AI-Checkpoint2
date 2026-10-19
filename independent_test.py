
from independent_scenarios import INDEPENDENT_SCENARIOS
from baseline import baseline_analyze
from three_level_baseline import three_level_analyze
from emt_ai import analyze_scenario

def run_independent_test():
    total = len(INDEPENDENT_SCENARIOS)

    original_correct = 0
    three_level_correct = 0
    emt_correct = 0

    print("\nEMT-AI INDEPENDENT TEST")
    print("=" * 85)

    for scenario in INDEPENDENT_SCENARIOS:
        title = scenario["title"]
        description = scenario["description"]
        expected = scenario["expected_priority"]

        original = baseline_analyze(description)
        three_level = three_level_analyze(description)
        emt = analyze_scenario(description)["priority"]

        if original == expected:
            original_correct += 1

        if three_level == expected:
            three_level_correct += 1

        if emt == expected:
            emt_correct += 1

        print(f"\nScenario: {title}")
        print(f"Expected: {expected}")
        print(f"Original Baseline: {original}")
        print(f"Three-Level Baseline: {three_level}")
        print(f"EMT-AI: {emt}")

    print("\nFINAL INDEPENDENT TEST RESULTS")
    print("=" * 85)

    print(
        f"Original Baseline: {original_correct}/{total} "
        f"({original_correct / total * 100:.1f}%)"
    )

    print(
        f"Three-Level Baseline: {three_level_correct}/{total} "
        f"({three_level_correct / total * 100:.1f}%)"
    )

    print(
        f"EMT-AI: {emt_correct}/{total} "
        f"({emt_correct / total * 100:.1f}%)"
    )

if __name__ == "__main__":
    run_independent_test()
