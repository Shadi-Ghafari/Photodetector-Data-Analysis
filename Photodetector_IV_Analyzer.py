import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
files = glob.glob("data/*current.xlsx")
plt.figure(figsize=(7,5))
colors =["black", "blue", "red", "green", "magenta", "orange"]
markers = ["o", "s", "^", "D", "v", "*"]
for i, file in enumerate(files):
    df = pd.read_excel(file)
    name = os.path.basename(file).replace(".xlsx", "")
    plt.plot(df["Smu1_V(1)(1)"], df["Smu1_I(1)(1)"], linewidth=0.9, color=colors[i % len(colors)], marker=markers[i % len(markers)], markersize=1.5, label=name)
plt.xlabel("Voltage (V)", fontsize=12)
plt.ylabel("Current (A)", fontsize=12)
plt.title("Photodetector I-V Curves", fontsize=14)
plt.grid(False)
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 12
plt.legend()
plt.savefig("results/IV_Curves.png", dpi=600, bbox_inches="tight")
plt.grid(False)
plt.show()