import pandas as pd
import matplotlib.pyplot as plt
import glob
dark_file = glob.glob("data/*dark*.xlsx")[0]
uv_file = glob.glob("data/*uv*.xlsx")[0]
df_dark = pd.read_excel(dark_file)
df_uv = pd.read_excel(uv_file)
voltage = df_dark["Smu1_V(1)(1)"]
Idark = df_dark["Smu1_I(1)(1)"]
Ilight = df_uv["Smu1_I(1)(1)"]
Iphoto = Ilight - Idark
Sensivity = (Iphoto / Idark) * 100
print("Photocurrent:")
print(Iphoto)
print("/nsensivity (%):")
print(Sensivity)
plt.figure(figsize=(7,5))
plt.plot(voltage, Iphoto, linewidth=2, marker="o")
plt.xlabel("Voltage (V)")
plt.ylabel("Photocurrent (A)")
plt.title("Photocurrent vs Voltage")
plt.grid(False)
plt.savefig("results/Photocurrent.png", dpi=600, bbox_inches="tight")
plt.show()