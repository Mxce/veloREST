from flask import Flask
import yaml
import requests
import csv
import pickle

from fitter import modelfitter

app = Flask(__name__)

addresses = yaml.safe_load(open("conf.yaml"))['addresses']

def get_fit_model(station_id):
	'''gets the trained model using modelfitter from imported module'''
	csv_as_text = requests.get(addresses['csvREST'] + '/stations/' + str(station_id)).text
	data = csv.read(csv_as_text)
	return modelfitter(data)

def fit_one(station_id):
	'''fits a model then POSTs it to predicrREST'''
	mod = get_fit_model(station_id)
	srlzd = pickle.dumps(mod)
	return requests.post(addresses['predictREST']+ '/updatemodel/' +str(station_id), srlzd)

@app.route('/')
def index():
    return "Ask for fitting with /fit/<station_id> OR /fitall"

@app.route('/fit/<int:station_id>')
def fit_station(station_id):
	return fit_one(station_id)
	
@app.route('/fitall')
def fit_all():
	#just a loop through station_id values given through a yaml file, and calling fit_one
	return 'not currently available'

if __name__ == '__main__':
    app.run(debug=True)
