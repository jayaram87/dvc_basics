from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import os
import yaml
import numpy as np

webapp_root = 'webapp'
params_path = 'params.yaml'

template_dir = os.path.join(webapp_root, 'templates')

app = Flask(__name__, template_folder=template_dir)


def predict(data):
    with open(params_path, 'r+') as f:
        config = yaml.safe_load(f)
    model_dir = config['webapp_model_dir']
    with open(model_dir, 'rb') as f:
        model = pickle.load(f)
    pred = model.predict(data)
    return np.round(pred, 2)


@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            tv = float(request.form['TV'])
            radio = float(request.form['radio'])
            newspaper = float(request.form['newspaper'])
            sales = predict(np.array([tv, radio, newspaper]).reshape(1, -1))
            print('sales is', sales)
            return render_template('result.html', prediction=round(sales[0], 2))
        except Exception as e:
            print('The Exception message is: ', str(e))
            return 'something is wrong'
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)