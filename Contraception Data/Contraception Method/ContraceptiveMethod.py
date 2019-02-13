import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/cmc/cmc.data"
headers = ["Wife Age", "Wife Edu", "Husband Edu", "Num Children", "Wife Religion", "Wife Working?",
"Husband Occupation", "Standard of Living Index", "Media Exposure", "Contraceptive Method Used"]
df = pd.read_csv(url, names=headers)
#print (df.head(40))

x = df["Wife Age"]
y1 = df["Wife Religion"]
y2 = df["Media Exposure"]
y3 = df["Contraceptive Method Used"]

y= np.vstack([y1, y2, y3])

labels = ["Religion", "Media Exposure", "Contraceptive Method"]

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels = labels)
ax.legend(loc= 'upper left')
plt.show()