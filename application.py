from flask import Flask,render_template,request
import pickle
import numpy as np

#create a Flask object
application = Flask(__name__)
'''@application.route('/')
def hello():
    """test function"""
    return "Welcome to the Flask"

@application.route('/saketh',methods=['GET'])
def check():
    """new function"""
    return "Codegnan is in KITS College"
'''
#First let's read the pickle file
with open('House_Price.pkl','rb') as f:
    model = pickle.load(f)
@application.route('/',methods=['GET'])
def home():
    return render_template('index.html')
@application.route('/predict',methods=['POST'])
def predict():
    Rooms = int(request.form['bedrooms'])
    Bathrooms = int(request.form['bathrooms'])
    Place = int(request.form['location'])
    Area = int(request.form['area'])
    Status = int(request.form['status'])
    Facing = int(request.form['facing'])
    P_Type = int(request.form['type'])
    #now take the above form data and convert to array
    input_data = np.array([[Place,Area,Status,Rooms,Bathrooms,Facing,P_Type]])
    #by taking above data we will predict the House_price
    prediction = model.predict(input_data)[0]
    #now we will pass above predicted data to template
    return render_template('index.html',prediction = prediction)
if __name__=="__main__":
    application.run()


