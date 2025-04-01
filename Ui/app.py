from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
model = joblib.load(r'D:\AI&ML Only\ML\flight-fair-prediction\best_model.pkl')
scaler = joblib.load(r'D:\AI&ML Only\ML\flight-fair-prediction\scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = {
        'airline': request.form['airline'],
        'flight': request.form['flight'],
        'source_city': request.form['source_city'],
        'departure_time': request.form['departure_time'],
        'stops': request.form['stops'],
        'arrival_time': request.form['arrival_time'],
        'destination_city': request.form['destination_city'],
        'class': request.form['class'],
        'duration': float(request.form['duration']),
        'days_left': int(request.form['days_left'])
    }

    # Convert to DataFrame
    input_data = pd.DataFrame(data, index=[0])

    # Encode the categorical variables (example mappings)
    mappings = {
        'airline': {'SpiceJet': 0, 'AirAsia': 1, 'Vistara': 2},  # Update with your mappings
        'flight': {'SG-8709': 0, 'I5-764': 1, 'UK-951': 2},  # Update with your mappings
        'source_city': {'Delhi': 0, 'Mumbai': 1, 'Bangalore': 2},  # Update with your mappings
        'departure_time': {'Evening': 0, 'Early_Morning': 1, 'Morning': 2},  # Update with your mappings
        'stops': {'zero': 0, 'one': 1},  # Update with your mappings
        'arrival_time': {'Night': 0, 'Morning': 1, 'Afternoon': 2},  # Update with your mappings
        'destination_city': {'Mumbai': 0, 'Delhi': 1, 'Bangalore': 2},  # Update with your mappings
        'class': {'Economy': 0, 'Business': 1}  # Update with your mappings
    }

    for col, mapping in mappings.items():
        input_data[col] = input_data[col].map(mapping)

    # Check for any unmapped values (This can be expanded as needed)
    if input_data.isnull().values.any():
        return render_template('index.html', prediction_text='Error: Some input values are invalid or not mapped.')

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_data_scaled)

    return render_template('index.html', prediction_text='Predicted Fare: ₹{:.2f}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)
