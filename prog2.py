import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

json_string = '{"nome" : "Somewhere Far Beyond", "dataLancamento" : new Date(1992, 5, 30), "duracao" : 3328, "artista" : {"nome" : "Blind Guardian"}}'
album = json.loads(json_string)

db.albuns.insert(album)