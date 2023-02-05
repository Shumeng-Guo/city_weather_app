# City Weather App

## Build images

```
cd city_to_zip && docker build -t cityzip . && cd ..
cd zip_to_weather && docker build -t zipweather . && cd ..
```

## Run the service with user-defined networking
# https://docs.docker.com/network/network-tutorial-standalone/
```
docker network create --driver bridge weather-net
docker run -d -p 5000:5000 --name city_to_zip --network weather-net cityzip
docker run -d -p 8080:8080 --name zip_to_weather --network weather-net zipweather
```