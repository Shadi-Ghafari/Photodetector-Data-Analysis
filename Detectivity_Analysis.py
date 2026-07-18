import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
files = glob.glob("data/*nm*.xlsx")
dark = pd.read_excel("data/dark_current.xlsx")
df = pd.read_excel(files[0])
import numpy as np
wavelength = []
detectivity = []
print(files)
print(df.columns)
for i, file in enumerate(files):
    df = pd.read_excel(file)
    wl = int(os.path.basename(file).split("nm")[0])
    wavelength.append(wavelength)
    idx = np.argmin(np.abs(df["Smu1_V(1)(1)"] -5))
power_density = 0.23e-3
area = 0.1
P = power_density * area
I_photo = df["Smu1_I(1)(1)"].iloc[idx] - dark["Smu1_I(1)(1)"].iloc[idx]
Responsivity = I_photo / P
Detectivity_measured = (Responsivity * np.sqrt(area))
print("Measured Detectivity (Jones)")
print(Detectivity_measured)
q = 1.602e-19
Idark = abs(dark["Smu1_I(1)(1)"])
shot_noise = np.sqrt(2*q*Idark)
Detectivity_shot = (Responsivity*np.sqrt(area))/shot_noise
print("shot_Noise Detectivity (Jones)")
print(Detectivity_shot)
plt.figure(figsize=(7,5))
plt.plot(wavelength, Detectivity_measured, marker="o", linewidth=1.5)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Detectivity (Jones)")
plt.title("Detectivity_measured vs wavelength")
plt.grid(False)
plt.savefig("results/Detectivity_vs_Wavelength.png", dpi=600, bbox_inches="tight")
plt.show()