from flask import Flask
from flask import request as frequest
import pickle

app = Flask(__name__)

dirname = 'MODELS'

@app.route('/')
def index():
    return "You can ask for a prediction using \n /predict?station_id&year&month&day&hour&weather\n A new model can also be posted"
	
@app.route('/predict/<int:station_id>')
def get_prediction(station_id):
	year= frequest.args.get('year')
	month= frequest.args.get('month')
	day= frequest.args.get('day')
	hour= frequest.args.get('hour')
	weather= frequest.args.get('weather')
	###############################################################
	predict = '?????'
	return( '/predict/' + str(station_id) 
		+'?'+ str(year)+'&'+ str(month)+'&'+ str(day)+'&'+ str(hour)+'&'+ str(weather))
	
@app.route('/updatemodel/<int:station_id>')
def update_model(station_id, methods = ['POST']):
	#ineficient to unpickle then pickle again, but… does it matter?
	srlzd = request.data
	model = pickle.load(srlzd)
	file = open(dirname + '/' + str(station_id), 'w')
	pickle.dump(model,file)
	###############################################################
	return 'model of station ' + station_id + ' updated successfuly!'

	
if __name__ == '__main__':
    app.run(debug=True)
