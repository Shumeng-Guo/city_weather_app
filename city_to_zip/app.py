from flask import Flask, request

app = Flask(__name__) 
@app.route('/')   # type: ignore
def index():
    return '<h1>City - Zipcode</h1> \
         <p>This website matches cities with cooresponding zipcodes</p>'


@app.route('/city') # type: ignore
def city_name():
    city = request.args.get('city')
    return f'The zipcode for {city} is : {city_zipcode[city]}' # type: ignore


city_zipcode = {'San Jose': 95131, 'Santa Clara': 95050, 'Fremont': 94539, 'Mountain View': 94041}



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)