import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.DataFrame({"Performance": ["Speed", "Handling", "Acceleration", "Launch", "Braking", "Offroad"], "Score": [10, 10, 6.9, 7.4, 9.0, 4.4]})
fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")

theta = np.arange(len(df) + 1) / float(len(df)) * 2 * np.pi

values = df["Score"].values
values = np.append(values, values[0])

l1, = ax.plot(theta, values, color="C2", marker="o", label="Score")
plt.xticks(theta[:-1], df["Performance"], color="grey", size=12)
ax.tick_params(pad=10)
ax.fill(theta, values, "green", alpha=0.1)

plt.style.use("seaborn-v0_8")
plt.title("Car Performance")
plt.savefig("./project/img/performanceChart.png")
plt.close()