import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ====================== CONFIG ======================

directory = Path(r'./battery_test_results')

# Output files
graph_output = directory / "combined_plot.png"
summary_output = directory / "combined_summary.xlsx"

# Find all raw.xlsx and summary.xlsx files
raw_files = sorted(directory.glob("*/raw.xlsx"))
summary_files = sorted(directory.glob("*/summary.xlsx"))

# ====================== GRAPH STYLES ======================

markers = [
    'o', 's', '^', 'D', 'v', 'P', 'X', '<', '>',
    'p', 'h', '*', 'd'
]

linestyles = [
    '-', '--', '-.', ':'
]

# ====================== PLOT GRAPH ======================

plt.figure(figsize=(12, 7))

for i, file in enumerate(raw_files):

    # Read raw.xlsx
    df = pd.read_excel(file)

    # Time(sec) -> Time(min)
    x = df.iloc[:, 0] / 60.0

    # Voltage(V)
    y = df.iloc[:, 1]

    # Subdirectory name
    label = file.parent.name

    # Plot
    plt.plot(
        x,
        y,

        linewidth=1.5,

        marker=markers[i % len(markers)],
        markersize=2.5,

        markevery=max(len(x) // 200, 1),

        linestyle=linestyles[i % len(linestyles)],

        alpha=0.9,

        label=label
    )

# ====================== GRAPH SETTINGS ======================

plt.xlabel("Time (min)", fontsize=12)
plt.ylabel("Voltage (V)", fontsize=12)

plt.ylim(3.0, 4.3)

plt.title("Voltage vs Time (Multiple Tests)", fontsize=14)

plt.legend(fontsize=9, loc='best')

plt.grid(True, linestyle='--', alpha=0.35)

plt.tight_layout()

# Save graph
plt.savefig(graph_output, dpi=300)

# Show graph
plt.show()

print(f"\n✅ Graph saved:")
print(graph_output)

# ====================== MERGE SUMMARY FILES ======================

summary_list = []

for file in summary_files:

    # Read summary.xlsx
    df = pd.read_excel(file)

    # Add directory name column
    df.insert(0, "Test_Name", file.parent.name)

    summary_list.append(df)

# Vertical stack
combined_summary = pd.concat(summary_list, ignore_index=True)

# Save merged summary
combined_summary.to_excel(summary_output, index=False)

print(f"\n✅ Combined summary saved:")
print(summary_output)