from flask import Flask
from flask import request as frequest
import pickle
import datetime
import os

app = Flask(__name__)

dirname = 'MODELS'

@app.route('/')
def index():
    return "You can ask for a prediction using \n /predict?station_id&year&month&day&hour&weather\n A new model can also be posted"
	
@app.route('/predict/<int:station_id>')
def get_prediction(station_id):
	year= int(frequest.args.get('year'))
	month= int(frequest.args.get('month'))
	day= int(frequest.args.get('day'))
	hour= int(frequest.args.get('hour'))
	weather= int(frequest.args.get('weather'))
	print(str(year) + str(month) + str(day))
	week= datetime.date(year,month,day).isocalendar()[1]
	
	path = dirname + '/' + str(station_id)
	
	###############################################################
	if os.path.exists(path):
		file= open(path, 'rb')
		mod=pickle.load(file)
		file.close()
		predict = mod.predict([[year,week, day,hour, weather]])
		return str(predict[0])		
	else:
		return 'model does not exist.. yet?'
	
@app.route('/updatemodel/<int:station_id>', methods = ['POST'])
def update_model(station_id):
	#ineficient to unpickle then pickle again, but.. does it matter?
	srlzd = frequest.data
	model = pickle.loads(srlzd)
	file = open(dirname + '/' + str(station_id), 'wb')
	pickle.dump(model,file)
	file.close()
	###############################################################
	return 'model of station ' + str(station_id) + ' updated successfuly!'

	
if __name__ == '__main__':
    app.run(debug=True)
