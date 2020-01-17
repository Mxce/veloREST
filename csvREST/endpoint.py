from flask import Flask, send_from_directory, send_file


dirname = 'CSV'

app = Flask(__name__)

@app.route('/')
def index():
    return "Ask for a CSV file using /station?station_id!"

@app.route('/stations/<int:station_id>')
def get_station(station_id):
	return send_from_directory(dirname, str(station_id) + 'class.csv')
	
#send_file(dirname + '/'+ str(station_id) + 'class.csv', as_attachment=False)
#send_from_directory(dirname, str(station_id) + 'class.csv')

if __name__ == '__main__':
    app.run(debug=True)
