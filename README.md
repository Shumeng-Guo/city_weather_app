# City Weather App

## Introduction

The City Weather App is an application that allows the users to find out the weather information given an input city name.
This application consists of two independent microservices:
  1. `city_to_zip` service - get the zipcode of the city given a city name
  <img width="311" alt="Screen Shot 2023-02-09 at 1 20 11 PM" src="https://user-images.githubusercontent.com/120552280/217941704-0edcf559-4d4f-4ee4-a3e7-2fc93bd018d8.png">
  
  2. `zip_to_weather` service - get the weather information in the area of a zipcode given an input of zipcode
  <img width="262" alt="Screen Shot 2023-02-09 at 1 21 08 PM" src="https://user-images.githubusercontent.com/120552280/217941865-24b06a3d-cb9d-4c61-8877-c9c64679ddc3.png">

Then, we build two Docker standalone containers for the two microservices respectively. \
Finally, to connect the two services, we build a Docker container network to let them talk to each other.

Thus in the end, the application will return the weather information when user gives a city name. 

---

## Clone the repository
```bash
git clone git@github.com:Shumeng-Guo/city_weather_app.git
```

---

## `city_to_zip` APP
### Build the Docker Image	

```bash
docker build -t cityzip .
```
<img width="865" alt="Screen Shot 2023-02-09 at 1 15 51 PM" src="https://user-images.githubusercontent.com/120552280/217940953-2299007f-c5d4-42b8-b2c2-f0294e5862b7.png">

### Run the INDEPENDENT container

```bash
docker run -d -p 5000:5000 cityzip
```

---

## `zip_to_weather` APP
### Build the Docker Image	

```bash
docker build -t zipweather .
```
<img width="848" alt="Screen Shot 2023-02-09 at 1 18 06 PM" src="https://user-images.githubusercontent.com/120552280/217941361-ffbb1952-58ca-4720-8fe0-9f7dcd6dffbe.png">

### Run the INDEPENDENT container

```bash
docker run -d -p 8080:8080 zipweather
```

---

## Networking: Make Two Containers Talk to Each Other

***Step 1***: Create a Docker user-defined network called `weather-net`

```bash
docker network create --driver bridge weather-net
```

***Step 2***: Run the two services with user-defined networking `weather-net`

```bash
docker run -d -p 5000:5000 --name city_to_zip --network weather-net cityzip
docker run -d -p 8080:8080 --name zip_to_weather --network weather-net zipweather
```
<img width="874" alt="Screen Shot 2023-02-09 at 1 26 13 PM" src="https://user-images.githubusercontent.com/120552280/217942824-3ba7a6d9-8585-4258-ad64-9421ae79b121.png">

### Testing
In our browser, type in localhost with port 5000 (from city_to_zip App config): \
<img width="258" alt="Screen Shot 2023-02-09 at 1 28 26 PM" src="https://user-images.githubusercontent.com/120552280/217943195-24e344d9-d9db-49bf-aedb-0af9a6fca5e7.png">

The result gives us the weather of the city 'San Jose' directly: \
<img width="449" alt="Screen Shot 2023-02-09 at 1 30 38 PM" src="https://user-images.githubusercontent.com/120552280/217943593-7e41a873-6509-434c-af2b-59fd92619021.png">

Meaning we have connected the two standalone services using Docker Network successfully!

---
