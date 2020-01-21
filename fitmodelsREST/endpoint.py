from flask import Flask
import yaml
import requests
import csv
import pickle
from io import StringIO

from fitter import modelfitter
from htmlgenerator import create_html

app = Flask(__name__)

addresses = yaml.safe_load(open("conf.yaml"))['addresses']

def get_fit_model(station_id, boolcluster = False):
	'''gets the trained model using modelfitter from imported module'''
	csv_as_text = requests.get(addresses['csvREST'] + '/stations/' + str(station_id)).text
	io = StringIO(csv_as_text)
	return modelfitter(io)
		
def fit_one(station_id):
	'''fits a model then POSTs it to predicrREST'''
	mod = get_fit_model(station_id)
	srlzd = pickle.dumps(mod)
	#io = BytesIO(srlzd)
	return requests.post(addresses['predictREST']+ '/updatemodel/' +str(station_id),srlzd).text
	
def send_html(station_id):
	csv_as_text = requests.get(addresses['csvREST'] + '/stationsclusters/' + str(station_id)).text
	io = StringIO(csv_as_text)
	html = create_html(io, station_id)
	return requests.post(addresses['clusterREST']+ '/updatehtml/' +str(station_id),html).text


@app.route('/')
def index():
    return "Ask for fitting with /fit/<station_id> OR /fitall"

@app.route('/fit/<int:station_id>')
def fit_station(station_id):
	return fit_one(station_id)
	
@app.route('/fitcluster/<int:station_id>')
def fit_cluster_station(station_id):
	return send_html(station_id)

	
@app.route('/fitall')
def fit_all():
	#just a loop through station_id values given through a yaml file, and calling fit_one
	return 'not currently available'

if __name__ == '__main__':
    app.run(debug=True)
