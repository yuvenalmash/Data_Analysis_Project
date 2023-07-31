from flask import Flask, request, jsonify
import joblib

file = '../notebooks/linear_regression_model.joblib'
model = joblib.load(file)

app = Flask(__name__)

@app.route('/predict_gdp_per_capita', methods=['POST'])
def predict_gdp_per_capita():
    try:
        data = request.get_json(force=True)
        continent = data.get('continent')
        population = data.get('population')
        gross_national_savings = data.get('gross_national_savings')
        features = data.get('features')

        if None in [continent, population, gross_national_savings, features]:
            return jsonify({'error': 'Missing required parameter'}), 400

        # Check for unexpected parameters
        unexpected_parameters = set(data.keys()) - {'continent', 'population', 'gross_national_savings', 'features'}
        if unexpected_parameters:
            return jsonify({'error': f'Unexpected parameter(s): {", ".join(unexpected_parameters)}'}), 400

        # Convert the features data to a 2D array
        features_array = [features]

        prediction = model.predict(features_array)[0]

        # Set the response headers to specify JSON content type
        response = jsonify({'predicted_gdp_per_capita': prediction})
        response.headers['Content-Type'] = 'application/json'

        return response, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Handle Method Not Allowed (405) explicitly for GET requests
@app.route('/predict_gdp_per_capita', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def method_not_allowed():
    return jsonify({'error': 'Method Not Allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
