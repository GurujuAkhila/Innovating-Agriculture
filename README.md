# Innovating-Agriculture
Technologically advanced Approach to Crop Management and Protection using IoT and AI
Agriculture is one of the most important resources for mankind. This project is about making the agriculture easier and effective by using the trending technologies like Artificial Intelligence (AI) and Internet of Things (IoT). 
The proposed model is designed in a such a way that it will let the farmer to know about the proper crop to grow that would give him the best yield according to soil pH and also helps in the crop monitoring by providing the status of the nutrients in the soil.

DESCRIPTION OF PROJECT:

1.Soil Testing:

 Using IoT sensors like Temperature sensor, Humidity sensor, NPK sensor interfacing with Raspberry   Pi, the parameters of the soil are measured and data is sent to user through mail.
  
  INTERFACING SOIL MOSITURE SENSOR WITH RASPBERRY PI:
  
  ![image](https://user-images.githubusercontent.com/125969582/220337959-6374a650-67f6-464b-9fdb-fd0bd4a4bda9.png)
  
  OUTPUT:
  
  (i) When there is need of water:
  
  ![image](https://user-images.githubusercontent.com/125969582/220339216-49847f2f-1c6e-43c6-8fab-2dd99740b599.png)
  
  (ii) when there is no need of water:
  
  ![image](https://user-images.githubusercontent.com/125969582/220339463-5b237545-9f84-4d04-9cef-5a9a7da8e9b5.png)

  INTERFACING DHT11 SENNOR With RASPBERRY PI:
  
  ![image](https://user-images.githubusercontent.com/125969582/220338555-a0b38254-081e-4ff2-8c11-d5429cb06b34.png)
  
  OUTPUT:
  
  ![image](https://user-images.githubusercontent.com/125969582/220339571-5eb127bf-c9f8-4ecc-b517-bfdc38e5a0f0.png)
  
  INTERFACING PI CAMERA WITH RASPBERRY PI:
  
  ![image](https://user-images.githubusercontent.com/125969582/220338767-a7ae6157-839f-4045-97be-f6ac5876c86e.png)
  
  OUTPUT:
  
  ![image](https://user-images.githubusercontent.com/125969582/220339675-1669bcbb-5db8-4f4a-8d31-60f4ca01c8d6.png)
  
  SENDING THE INFORMATION TO MAIL:
  
  ![image](https://user-images.githubusercontent.com/125969582/220338969-4dab3410-c63b-4f1d-9df3-46661240156f.png)

2.Crop Recommender:

  It uses ‘data set’, A data set contains soil parameters data like N, P, K, pH, moisture content,   humidity, temperature. Crop Recommender compares the data given against the dataset and suggests   the best crops that can be grown with the help sensors like soil pH, soil moisture and soil         temperature senor. Here Gradient Boosting Algorithm is used.
  
3.Fertilizer Recommender

  It uses the ‘Nutrition dataset’, A nutrition data set contains the parameters like ratio of N, P,   K. It compares the data collected from IoT sensors against the nutrition dataset and tells the     fertility rate of the given samples. Fertilizer Recommender suggests the Fertilizer required for   the best yield possible. Here Gradient Boosting Algorithm is used.
  
  
