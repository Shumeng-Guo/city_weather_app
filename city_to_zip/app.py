
from flask import Flask, request
import requests

app = Flask(__name__) 
@app.route('/')
def index():
    return '<h1>City - Zipcode</h1> \
         <p>This website matches cities with cooresponding zipcodes</p>'


@app.route('/city')
def test():
    city = request.args.get('city') or ''
    zip = city_zipcode.get(city, '')
    weather = requests.get(f'http://zip_to_weather:8080/zipcode?zipcode={zip}').text.split()[-1]
    return f'The zipcode for {city} is : {city_zipcode[city]}, and the weather is : {weather}.'

city_zipcode = {'San Jose': 95131, 'Santa Clara': 95050, 'Fremont': 94539, 'Mountain View': 94041}



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)