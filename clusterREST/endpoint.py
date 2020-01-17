from flask import Flask
from flask import request as frequest

app = Flask(__name__)

dirname = ''

@app.route('/')
def index():
    return "You can ask for a clustering using \n /cluster/station_id"
	
@app.route('/cluster/<int:station_id>')
def get_prediction(station_id):
	###############################################################
	return( '/predict/' + str(station_id) 
		+'?'+ str(year)+'&'+ str(month)+'&'+ str(day)+'&'+ str(hour)+'&'+ str(weather))
	
@app.route('/updatemodel/<int:station_id>')
def update_model(station_id, methods = ['POST']):
	###############################################################
	return 'model of station ' + station_id + ' updated successfuly!'

	
if __name__ == '__main__':
    app.run(debug=True)
