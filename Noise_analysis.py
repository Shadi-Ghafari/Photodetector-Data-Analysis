import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
files = glob.glob("data/*I-t Zif67*.xlsx")
df = pd.read_excel(files[0])
import numpy as np
current = df["Smu1_I(1)(1)"]
noise = current - np.mean(current)
noise_rms = np.std(current)
print("RMS Noise Current =", noise_rms, "A")
plt.figure(figsize=(7,5))
plt.plot(df.iloc[:,0], df.iloc[:,1], linewidth=1)
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("Current-Time Curve")
plt.grid(False)
plt.show()
plt.plot(df["Smu1_Time(1)(1)"], noise)
plt.xlabel("Time (s)")
plt.ylabel("Noise Current (A)")
plt.title("Noise Signal")
plt.grid(False)
plt.show()