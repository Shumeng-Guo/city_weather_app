import requests

def combine_service(city_name):
    # get the zipcode of the city from city_to_zip service
    zip_code = requests.get(f'http://127.0.0.1:5000/city?city={city_name}')  # type: ignore
    zip = zip_code.text.split()[-1]
    print(zip_code.text)
    
    # get the weather of the city from weather service using the zipcode retrived
    weather = requests.get(f'http://127.0.0.1:8080/zipcode?zipcode={zip}').text  # type: ignore


    return weather

if __name__ == '__main__':
    print('Welcome to the weather service!')
    print('Available cities for weather checkup:')
    print('San Jose, Santa Clara, Fremont, Mountain View')
    city_name = input('Enter the name of a city: ')
    print(combine_service(city_name))