from flask import Flask
from flask import request as frequest
import yaml
import requests

app = Flask(__name__)

addresses = yaml.safe_load(open("conf.yaml"))['addresses']

@app.route('/')
def index():
    return "You can fit the models, predict a value or ask for clustering data use /predict?station_id&year&month&day&hour&weather\nOR /fit\nOR /cluster?station_id"

#this should be protected...
@app.route('/fit')
def fit():
	#SENDING REQUEST TO fitmodelREST
	return requests.get(addresses['fitmodelsREST'] + '/fit')
	
@app.route('/predict/<int:station_id>')
def get_prediction(station_id):
	year= frequest.args.get('year')
	month= frequest.args.get('month')
	day= frequest.args.get('day')
	hour= frequest.args.get('hour')
	weather= frequest.args.get('weather')
	#SENDING REQUEST TO predictREST
	return requests.get(addresses['predictREST'] + '/predict/' + str(station_id),
		params={'year': year, 'month': month, 'day': day, 'hour': hour, 'weather': weather}).text


@app.route('/cluster/<int:station_id>')
def get_cluster(station_id):
	#SENDING REQUEST TO clusterREST
	return requests.get(addresses['clusterREST'] + '/cluster/' + str(station_id)).text
	
if __name__ == '__main__':
    app.run(debug=True)
