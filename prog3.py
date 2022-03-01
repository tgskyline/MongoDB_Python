import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

album = db.albuns.find_one({"nome" : "Somewhere Far Beyond"})

nome = album["artista"]["nome"]
print(nome)