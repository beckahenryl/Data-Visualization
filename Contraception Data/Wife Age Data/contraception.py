import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/cmc/cmc.data"
headers = ["Wife Age", "Wife Edu", "Husband Edu", "Num Children", "Wife Religion", "Wife Working?",
"Husband Occupation", "Standard of Living Index", "Media Exposure", "Contraceptive Method Used"]
df = pd.read_csv(url, names=headers)
#print (df.head(40))

num_bins = 10
n, bins, patches = plt.hist(df["Wife Age"], num_bins, facecolor = 'teal', alpha= 0.5)
plt.show()

