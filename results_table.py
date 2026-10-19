
import csv

from scenarios import SCENARIOS
from baseline import baseline_analyze
from three_level_baseline import three_level_analyze
from emt_ai import analyze_scenario

# Store the results for all three systems.
results = []

print("\nEMT-AI THREE-MODEL COMPARISON")
print("=" * 105)

print(
    f"{'Scenario':<32}"
    f"{'Expected':<12}"
    f"{'Original':<12}"
    f"{'Three-Level':<14}"
    f"{'EMT-AI':<12}"
)

print("-" * 105)

for scenario in SCENARIOS:
    title = scenario["title"]
    description = scenario["description"]
    expected = scenario["expected_priority"]

    original = baseline_analyze(description)
    three_level = three_level_analyze(description)
    emt = analyze_scenario(description)["priority"]

    results.append({
        "Scenario": title,
        "Expected": expected,
        "Original Baseline": original,
        "Three-Level Baseline": three_level,
        "EMT-AI": emt
    })

    print(
        f"{title[:30]:<32}"
        f"{expected:<12}"
        f"{original:<12}"
        f"{three_level:<14}"
        f"{emt:<12}"
    )

print("\nFINAL COMPARISON")
print("=" * 50)

for name, key in [
    ("Original Baseline", "Original Baseline"),
    ("Three-Level Baseline", "Three-Level Baseline"),
    ("EMT-AI", "EMT-AI")
]:
    correct = sum(
        row[key] == row["Expected"]
        for row in results
    )

    total = len(results)
    accuracy = 100 * correct / total if total else 0

    print(f"{name}: {correct}/{total} ({accuracy:.1f}%)")

# Save results to a CSV file.
with open("comparison_results.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Scenario",
            "Expected",
            "Original Baseline",
            "Three-Level Baseline",
            "EMT-AI"
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print("\nResults saved to comparison_results.csv")
