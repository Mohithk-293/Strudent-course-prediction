from flask import Flask, render_template, redirect, url_for,request,flash, session,jsonify
from getresults import *
from flask_session import Session
from flask import make_response
from flask_cors import CORS
app = Flask(__name__,template_folder='template')
CORS(app)
# Your existing back-end code for preprocessing and predicting branches
# ... (paste your back-end code here)

# Define a route to serve the index.html file
@app.route('/')
def index():
    return render_template('admission.html')

# Define a route to handle the form submission and return predicted branches
@app.route('/predict', methods=['POST'])
def predict():
   rank = int(request.form['rank'])
   category = int(request.form['category'])
   print(category)

    # Call the branch prediction function (from your existing back-end code)
   predicted_branches = predict_course([rank, category], 2)  # Change '3' to the desired number of predictions
   print(predicted_branches)
   return jsonify(predicted_branches)
if __name__ == '__main__':
    app.run(debug=True,port=53020,host="0.0.0.0")
