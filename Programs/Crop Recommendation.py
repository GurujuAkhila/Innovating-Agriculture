import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

dataset = pd.read_csv(r'F:\Clg\5th sem\Research internship\Research Internship (Github)\Datasets\Crop_recommendation.csv')

features = dataset[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
label = dataset["label"]

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2)

model = GradientBoostingClassifier()
model.fit(features, label)

input_values = [80, 40, 35, 30, 35, 4, 100]

pred_crop = model.predict([input_values])
y_pred = model.predict(X_test)

print("The recommended crop is: ", pred_crop[0])
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy*100)


