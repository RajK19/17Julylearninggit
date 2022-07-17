import pymongo

# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

client = pymongo.MongoClient("mongodb+srv://RajKansal:rajmongo19@legionx.fa7rw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

dict = {

    "name": "raj",
    "email": "rajkansal2001@gmail.com",
    "surname" : "kansal"

}

databs = client['mongotest']
coll = databs['test']
coll.insert_one(dict)