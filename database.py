from pymongo import MongoClient
import certifi

MONGO_URI ="mongodb+srv://vercel-admin-user:cc0tQeO4FGtjhfrS@cluster0.huz0q2x.mongodb.net/?retryWrites=true&w=majority"
ca = certifi.where()


def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_productos_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db

