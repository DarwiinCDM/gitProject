from pymongo import MongoClient
import certifi

monogo_uri = 'mongodb+srv://darwinsmontoya:1010172043@cluster0.6pxpkqc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
ca = certifi.where()

def dbConection():
    try: 
        client = MongoClient.connect(monogo_uri, tlsCAFile=ca)
        db = client["database_gitproject"]
    except ConnectionError:
        print('No se ha podido conectar a la base de datos')
    return db
