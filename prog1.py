import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

albuns = db.albuns.find()

file = open("C:\\Users\\Tiago Gomes\\OneDrive\\Documentos\\Pos BI&A\\Bancos de dados relacionais e não-relacionais\\Python_MongoBD\\albuns.txt", "a")

for item in albuns:
    nome = item["nome"]
    file.write(nome + '\n')

file.close()