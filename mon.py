import pymongo as py
client = py.MongoClient()
db=client['Student']
collection=db['Student']
for i in range(0):
    name=input("Enter name")
    mark=int(input("Enter Marks"))
    if(mark>=0 and mark<101):
        collection.insert_one({'Name':name,'Marks':mark})
data=collection.find({'Marks':{'$gt':80}})
for i in data:
    print(i)
