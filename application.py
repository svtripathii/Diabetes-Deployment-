from flask import Flask, request, render_template
import pickle
import numpy as np

application = Flask(__name__)
app = application

# Load models and scaler
scaler = pickle.load(open("Model/standardScalar.pkl", "rb"))
model = pickle.load(open("Model/modelForPrediction.pkl", "rb"))

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for Single data point prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""
    if request.method == 'POST':
        # Get form data
        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        # Scale input data
        new_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        predict = model.predict(new_data)

        # Generate result
        result = 'Diabetic' if predict[0] == 1 else 'Non-Diabetic'

        return render_template('single_prediction.html', result=result)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
