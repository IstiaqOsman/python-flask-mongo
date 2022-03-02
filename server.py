from flask import Flask, Response, request
import pymongo
import json
app = Flask(__name__)
try:
    mongo = pymongo.MongoClient(
        host =  "localhost", 
        port = 27017,
    # serverSeleectionTimeoutMS = 1000
    )
    
    db = mongo.company

#trigger exception if cannot connect to db
    mongo.server_info()


except:
    print("Error - cannot connect to db")
##############################

@app.route("/users", methods = ['POST'])
def create_user():
    try: 
        user = {
            "name":request.form["name"], 
            "lastName":request.form["lastName"]
            }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response= json.dumps(
                {
                "message":"user created",
                "id":f"{dbResponse.inserted_id}"
                }
            ),
            status= 200,
            mimetype="application/json"
        )

    except Exception as ex:
        print("*********")
        print(ex)
        print("*********")

##############################

if __name__ == "__main__":
    app.run(port=5555, debug = True)