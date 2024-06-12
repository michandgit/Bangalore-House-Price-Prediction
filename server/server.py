from flask import Flask , request , jsonify 
# from flask_cors import CORS
import util

app = Flask(__name__)
# CORS(app)

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/get_location_names")
def get_location_names():
    response  = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access Control Allow Origin' , '*')
    return response

@app.route('/predict_home_price' , methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location ,total_sqft ,bhk,bath)
    })
    response.headers.add('Access Control Allow Origin' , '*')
    return response
    

if __name__ == "__main__":
    print("Starting Python Flask server for Home Price Prediction")
    util.load_saved_artifacts()
    app.run() 