from flask import Flask, request, render_template, jsonify
from dht import DHT11
from db import Database
import time

app = Flask(__name__)

dht11 = DHT11.DHT11()
humtemp = dht11.getdht()
dhtdb = Database.Database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/insertdb')
def insertdb():
    result = dhtdb.insertJson(humtemp[1], humtemp[0])
    if result in "good":
        return jsonify('{"temp"'+':"'+str(humtemp[0])+'"'+', "hum"'+':"'+str(humtemp[1])+'"}')
    else:
        return jsonify('{"error":"error"}')


@app.route('/selectdb')
def selectdb():
    result = dhtdb.selectAllJson()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

