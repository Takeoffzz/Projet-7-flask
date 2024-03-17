from flask import Flask,render_template,request
from flask_restful import Api, Resource, reqparse
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
from joblib import dump, load

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def home():
    dataframe = pd.read_csv('app_train.csv')
    col = 'TARGET'
    X = dataframe.loc[:, dataframe.columns != col]
    y = dataframe['TARGET']
    model = load('LGBM_TUNED.joblib')

    return X, y, model

X, y, model = home()
    

@app.route("/predict",methods=["GET"])
def predict():
    id = request.form['id']
    if (X['SK_ID_CURR'] == id).any() :
        form_array = X[X['SK_ID_CURR'] == id]
        prediction = model.predict(form_array)
        if prediction >= 0.478:
            result = print(f"Score du client : {prediction}, le crédit peut-être accordé.")
        else:
            result = print(f"Score du client : {prediction}, ne pas accorder de crédit.")
    else:
        result = print(f"Pas de client renseigné avec cet ID.")
        
    return render_template("result.html",result = result)


class DemoApiEndpoint(Resource):
    def __init__(self):
        self.post_args = reqparse.RequestParser()
        self.post_args.add_argument("name",
                                    type=str,
                                    help="You must include a name string with this post request.",
                                    required=True)
    def get(self):
        return {
            "message": "This is a response from a GET request."
        }

    def post(self):
        args = self.post_args.parse_args()
        name = args['name']
        return {
            "message": f'Nice to meet you, {name}!'
        }

api.add_resource(DemoApiEndpoint, "/api/DemoApiEndpoint")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
            

