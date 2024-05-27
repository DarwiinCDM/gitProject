import os
from flask import Flask, send_file, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def index():
    # return send_file('index.html')
    return '<h1> Hello worldd </h1>'

@app.route("/getRes", methods= ['GET'])
def RecibirRegistros():
    # print(request.json)
    return 'recived'

@app.route("/addReg", methods=['POST'])
def CrearRegistro():
    return 'recibed'

def main():
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
