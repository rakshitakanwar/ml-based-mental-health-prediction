from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os
app = Flask(__name__)
# Load trained model
model = joblib.load("model.pkl")
# Home page
@app.route("/")
def home():
    return render_template("index.html")
# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Get input values
    screen_hours = float(data["screen_hours"])
    sleep_hours = float(data["sleep_hours"])
    gender = int(data["gender"])
    # Same order as training features
    input_data = np.array([
        [
            screen_hours,
            sleep_hours,
            gender
        ]
    ])
    # Prediction
    prediction = model.predict(input_data)
    # Convert output
    if prediction[0] == 1:
        result = "Depressed"
    else:
        result = "Not Depressed"


    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )