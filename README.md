# Diabetes-Deployment-

This project demonstrates the deployment of a machine learning model to predict diabetes. The project uses Python for data processing and model building, and Flask for serving the model as a web application.

## Project Structure

 ├── app.py # Flask application 
 
 ├── model.py # Script for training the machine learning model 
 
 ├── static/  │ 
 
 └── styles.css # CSS styling for the web interface 
   
 ├── templates/ │   
   └── index.html # HTML template for the web interface 
   
   ├── model.pkl # Pre-trained machine learning model 
   
├── README.txt # Project documentation 

└── requirements.txt # Python dependencies


## Requirements

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- scikit-learn
- pandas
- numpy
- gunicorn (for deployment)

You can install the necessary packages using `pip`:

pip install -r requirements.txt


## Usage

1. **Train the Model:**
   - Run `model.py` to train the machine learning model using the provided dataset. This will create a `model.pkl` file.

2. **Run the Application:**
   - Run `app.py` to start the Flask web application:
- The application will be available at `http://127.0.0.1:5000/`.

3. **Deploying the Application:**
- Use `gunicorn` for deployment on production servers. To deploy using gunicorn, run:


## Web Interface

The web application provides a simple user interface where users can input health-related metrics (e.g., glucose levels, blood pressure) and receive a prediction on whether the person is likely to have diabetes.

## Acknowledgments

- The dataset used for model training was taken from [Kaggle's Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database).
- This project is inspired by the practical applications of machine learning in healthcare.



