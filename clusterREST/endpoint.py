from flask import Flask, send_from_directory
from flask import request as frequest

dirname = 'HTML/'

app = Flask(__name__)

@app.route('/')
def index():
    return "You can ask for a clustering using \n /cluster/station_id"

@app.route('/cluster/<int:station_id>')
def get_prediction(station_id):
	###############################################################
	print('seding cluster ' + str(station_id))
	return send_from_directory(dirname, str(station_id) + '.html')

@app.route('/updatehtml/<int:station_id>', methods = ['POST'])
def update_html(station_id):
	srlzd = frequest.data
	file = open(dirname + str(station_id) + '.html', 'wb')
	file.write(srlzd)
	file.close()
	###############################################################
	return 'html of station ' + str(station_id) + ' updated successfuly!'


if __name__ == '__main__':
    app.run(debug=True)
