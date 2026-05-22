import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ====================== 설정 ======================
directory = r'./test_result'

# 폴더 내 모든 xlsx 파일 가져오기
files = sorted(Path(directory).glob("*.xlsx"))

# ==================== markers 확장 ====================
markers = [
    'o', 's', '^', 'D', 'x', '*', 'v', '+', 'p', 'h',
    '<', '>', 'P', 'H', 'X', 'd', '|', '_',
    '1', '2', '3', '4'
]

# 그래프 생성
plt.figure(figsize=(11, 7))

for i, file in enumerate(files):

    df = pd.read_excel(file)
    
    # 초 → 분 변환
    x = df.iloc[:, 0] / 60.0
    y = df.iloc[:, 1]
    
    label = file.stem

    plt.plot(
        x, y,
        marker=markers[i % len(markers)],
        markersize=1.5,
        linewidth=0.7,
        alpha=0.75,
        label=label
    )

# ==================== 그래프 설정 ====================
plt.xlabel("Time (min)")
plt.ylabel("Voltage (V)")

plt.ylim(3.0, 4.3)
plt.title("Voltage vs Time (Multiple Tests)")

plt.legend(fontsize=9, loc='best')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()