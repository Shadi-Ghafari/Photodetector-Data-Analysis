import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
files = glob.glob("data/*I-t Zif67*.xlsx")
df = pd.read_excel(files[0])
import numpy as np
for i, file in enumerate(files):
    df = pd.read_excel(file)
    name = os.path.basename(file).replace(".xlsx", "")
    print(name)
    if "dark" in name.lower(): df_dark = df
    elif "uv" in name.lower(): df_uv = df
power_density = 0.23e-3
area = 0.1
P = power_density * area
I_photo = df_uv["Smu1_I(1)(1)"] - df_dark["Smu1_I(1)(1)"]
Responsivity = I_photo / P
print(Responsivity)
plt.figure(figsize=(7,5))
plt.plot(df_uv["Smu1_V(1)(1)"], Responsivity, color="red", linewidth=2, marker="o", markersize=4)
plt.xlabel("Voltage (V)")
plt.ylabel("Responsivility (A/W)")
plt.title("Responsivility vs Voltage")
plt.grid(False)
plt.show()