import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
files = glob.glob("data/*I-t*.xlsx")
df = pd.read_excel(files[0])
time = df["Smu1_Time(1)(1)"]
current = df["Smu1_I(1)(1)"]
I_max = current.max()
I_min = current.min()
print("Maxium Current =", I_max)
print("Minimum Current =", I_min)
I10 = I_min + 0.1*(I_max - I_min)
I90 = I_min + 0.9*(I_max - I_min)
print("10% =", I10)
print("90% =", I90)
t10 = time[current >= I10].iloc[0]
t90 = time[current >= I90].iloc[0]
rise_time = t90 - t10
print("Rise Time =", rise_time, "s")
t90_fall = time[current[::-1] >= I90].iloc[-1]
t10_fall = time[current[::-1] >= I10].iloc[-1]
fall_time =t10_fall
Ion = current.max() - t90_fall
print("Fall Time =", fall_time, "s")
Ioff = current.min()
on_off_ration = Ion / Ioff
print("Ion =", Ion, "A")
print("Ioff =", Ioff, "A")
print("on/off Ration =", on_off_ration)
first_current = current.iloc[0]
last_current = current.iloc[-1]
stability = (last_current / first_current) * 100
print("Stability =", stability, "%")
plt.figure(figsize=(8,5))
plt.plot(time, current, linewidth=1.5)
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("Current-Time Curve")
plt.grid(False)
plt.show()
results = {"Parameter": ["Rise Time (s)", "Fall Time (s)", "On/Off Ration", "Stability (%)"], "Value": [rise_time, fall_time, on_off_ration, stability]}
results_df = pd.DataFrame(results)
results_df.to_excel("results/Analysis_Results.xlsx", index=False)
print("Results saved successfully!")