import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("cbc_dataset_project.csv")

X = df[['hemoglobin', 'wbc', 'platelets', 'rbc']]
y = df['disease']

model = RandomForestClassifier()
model.fit(X, y)

def predict(data):
    return model.predict([data])[0]
