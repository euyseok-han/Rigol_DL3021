import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ====================== CONFIG ======================
directory = Path(r'./test_result')

# Find all raw.xlsx files inside subdirectories
files = sorted(directory.glob("*/raw.xlsx"))

# ====================== STYLES ======================

# Distinct marker styles
markers = [
    'o', 's', '^', 'D', 'v', 'P', 'X', '<', '>',
    'p', 'h', '*', 'd'
]

# Distinct line styles
linestyles = [
    '-', '--', '-.', ':'
]

# Create figure
plt.figure(figsize=(12, 7))

for i, file in enumerate(files):

    # Read raw.xlsx
    df = pd.read_excel(file)

    # Time(sec) -> Time(min)
    x = df.iloc[:, 0] / 60.0

    # Voltage(V)
    y = df.iloc[:, 1]

    # Use subdirectory name as label
    label = file.parent.name

    # Plot
    plt.plot(
        x,
        y,

        # Smoother line
        linewidth=1.5,

        # Marker style
        marker=markers[i % len(markers)],

        # Smaller markers
        markersize=2.5,

        # MUCH denser markers
        markevery=max(len(x) // 200, 1),

        # Line style variation
        linestyle=linestyles[i % len(linestyles)],

        alpha=0.9,

        label=label
    )

# ====================== GRAPH SETTINGS ======================

plt.xlabel("Time (min)", fontsize=12)
plt.ylabel("Voltage (V)", fontsize=12)

plt.ylim(3.0, 4.3)

plt.title("Voltage vs Time (Multiple Tests)", fontsize=14)

# Better legend
plt.legend(fontsize=9, loc='best')

# Cleaner grid
plt.grid(True, linestyle='--', alpha=0.35)

plt.tight_layout()

plt.show()