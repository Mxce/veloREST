from flask import Flask, send_from_directory

dirname = ''

app = Flask(__name__)

@app.route('/')
def index():
    return "You can ask for a clustering using \n /cluster/station_id"
	
@app.route('/cluster/<int:station_id>')
def get_prediction(station_id):
	###############################################################
	return send_from_directory(dirname, str(station_id) + '.html')
	
if __name__ == '__main__':
    app.run(debug=True)
