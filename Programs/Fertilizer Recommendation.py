import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

# Load the dataset
data = pd.read_csv(r'F:\Clg\5th sem\Research internship\Research Internship (Github)\Datasets\Fertilizer Prediction.csv')

# Split the data into features and target
features = data[["Temperature", "Humidity ", "Moisture", "Nitrogen", "Potassium", "Phosphorous"]]
target = data["Fertilizer Name"]

# Train the Gradient Boosting model
model = GradientBoostingClassifier()
model.fit(features, target)

#input values
input_values = [30, 20, 15, 10, 15, 10]
predicted_fertilizer = model.predict([input_values])
print("The recommended fertilizer is: ", predicted_fertilizer[0])
