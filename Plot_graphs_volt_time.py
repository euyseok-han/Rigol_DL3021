import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ====================== CONFIG ======================
directory = Path(r'./test_result')

# Find all raw.xlsx files inside subdirectories
files = sorted(directory.glob("*/raw.xlsx"))

# ====================== MARKERS ======================
markers = [
    'o', 's', '^', 'D', 'x', '*', 'v', '+', 'p', 'h',
    '<', '>', 'P', 'H', 'X', 'd', '|', '_',
    '1', '2', '3', '4'
]

# Create figure
plt.figure(figsize=(11, 7))

for i, file in enumerate(files):

    # Read raw.xlsx
    df = pd.read_excel(file)

    # First column = Time(sec)
    x = df.iloc[:, 0] / 60.0   # Convert sec -> min

    # Second column = Voltage(V)
    y = df.iloc[:, 1]

    # Use subdirectory name as legend label
    label = file.parent.name

    # Plot graph
    plt.plot(
        x,
        y,
        marker=markers[i % len(markers)],
        markersize=1.5,
        linewidth=0.7,
        alpha=0.75,
        label=label
    )

# ====================== GRAPH SETTINGS ======================

plt.xlabel("Time (min)")
plt.ylabel("Voltage (V)")

plt.ylim(3.0, 4.3)

plt.title("Voltage vs Time (Multiple Tests)")

plt.legend(fontsize=9, loc='best')

plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

plt.show()