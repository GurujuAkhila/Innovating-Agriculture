# Innovating-Agriculture
Technologically advanced Approach to Crop Management and Protection using IoT and AI
Agriculture is one of the most important resources for mankind. This project is about making the agriculture easier and effective by using the trending technologies like Artificial Intelligence (AI) and Internet of Things (IoT). 
The proposed model is designed in a such a way that it will let the farmer to know about the proper crop to grow that would give him the best yield according to soil pH and also helps in the crop monitoring by providing the status of the nutrients in the soil.

DESCRIPTION OF PROJECT:
1.Soil Testing: 
  Using IoT sensors like Temperature sensor, Humidity sensor, NPK sensor interfacing with Raspberry   Pi, the parameters of the soil are measured and data is sent to user through mail.
  
  ![image](https://user-images.githubusercontent.com/125969582/220337959-6374a650-67f6-464b-9fdb-fd0bd4a4bda9.png)

2.Crop Recommender: 
  It uses ‘data set’, A data set contains soil parameters data like N, P, K, pH, moisture content,   humidity, temperature. Crop Recommender compares the data given against the dataset and suggests   the best crops that can be grown with the help sensors like soil pH, soil moisture and soil         temperature senor. Here Gradient Boosting Algorithm is used.
3.Fertilizer Recommender
  It uses the ‘Nutrition dataset’, A nutrition data set contains the parameters like ratio of N, P,   K. It compares the data collected from IoT sensors against the nutrition dataset and tells the     fertility rate of the given samples. Fertilizer Recommender suggests the Fertilizer required for   the best yield possible. Here Gradient Boosting Algorithm is used.
  
  
