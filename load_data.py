import numpy as np
import pandas as pd


df = pd.read_csv(FILE_NAME, delimiter=",")
data = df.to_numpy()

n_samples, n_features = data.shape
n_features -= 1

X = data[:, 0: n_features]
y = data[:, n_features]

print(X.shape)
print(y.shape)