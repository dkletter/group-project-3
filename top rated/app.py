from flask import Flask, jsonify
import pymongo
import os

# Create instance of Flask app
app = Flask(__name__)


# Setup connection to MongoDB database on MongoDB locally
conn = os.environ.get('mongodb://localhost:27017')

# Initialize PyMongo to work with MongoDBs. 
client = pymongo.MongoClient(conn)


# connect to mongo db and collections
db = client.restaurant_db
restaurant = db.restaurant


# Create route that renders index.html template
@app.route("/")
def welcome():
    with open('index.html') as f:
        return f.read()


# Add api route to get restaurant json
@app.route("/api/v1.0/restaurant")
def restaurantdata():
    # Convert all documents in the restaurant collection to a list
    records = list(restaurant.find())

    # Convert mongo id object to string
    for record in records:
        record["_id"] = str(record["_id"])
    
    # Return the json representation of the records
    return jsonify(records)



if __name__ == "__main__":
    app.run(debug=True)