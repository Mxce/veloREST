import pandas
import plotly.express as px

import plotly.io as pio
from sklearn.cluster import DBSCAN


def getData(dataset):
    array = []
    for i in range(0,len(dataset)):
            lat = dataset[1][i]
            long = dataset[2][i]
            nb = dataset[3][i]
            array.append([lat,long,nb])
    return array

def html_from_data(data,pred,title):
    x=[]
    y=[]
    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])

    fig = px.scatter(x=x,y=y,color=pred)
    fig.update_layout(title=title)
    return pio.to_html(fig)

def create_html(f, id):
	ds = pandas.read_csv(f,header=None)
	arrayData = getData(ds)
	dbscan = DBSCAN(eps=4,min_samples=2)
	dbscan.fit(arrayData)
	pred = dbscan.fit_predict(arrayData)
	return html_from_data(arrayData,pred,'clusters for station' + str(id))

