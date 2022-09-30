from pymongo import MongoClient
import os


USER_NAME = os.getenv("USER_NAME")
USER_PWD = os.getenv("USER_PWD")
DB_URL = os.getenv("DB_URL")
mongoUrlK8s = f"mongodb://{USER_NAME}:{USER_PWD}@{DB_URL}"
client = MongoClient(mongoUrlK8s)
#create collection
db = client["users"]

collection = db["new_users"]
#declare two records
user_1 = {
  "id" : "1",
  "user_name" : "Erick",
  "hometown" : "Nairobi"
}

user_2 = {
  "id" : "2",
  "user_name" : "Perry",
  "hometown" : "Bameda"
}
#insert into new users collection
collection.insert_many([user_1,user_2])

user_details = collection.find()
print("The users in this collection are: ")
for user in user_details:
   print(user['id'],user['user_name'], user['hometown'])