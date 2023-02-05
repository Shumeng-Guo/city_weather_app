from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Zipcode - Weather</h1> \
    <p>This website matches zipcode with cooresponding area weather</p>'


@app.route('/zipcode')
def city_name():
    zip_code = request.args.get('zipcode') or ''
    return f'The weather for {zip_code} is : {zipcode_weather[zip_code]}'


zipcode_weather = {'95131': 'Rainy', '95050': 'Sunny', '94539': 'Sunny', '94041': 'Rainy'}



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)