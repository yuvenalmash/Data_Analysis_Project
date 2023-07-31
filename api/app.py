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

        prediction = model.predict([[continent, population, gross_national_savings, features]])

        return jsonify({'predicted_gdp_per_capita': prediction[0]}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
    
