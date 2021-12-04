import pymongo
from flask import Flask, jsonify, render_template
from pymongo import MongoClient

# Create instance of Flask app
app = Flask(__name__)

# Initialize pymongo to work with mongodb
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.portland_db
collection = db.restaurants

# Route to render index
@app.route("/")
def home():
    with open("index.html") as f:
        return f.read()

# Route to render geojson
@app.route("/json")
def get_geojson():
    # Convert all documents in the restaurant collection to a list
    records = list(collection.find())

    # Convert mongo id object to string
    for record in records:
        record["_id"] = str(record["_id"])
    
    # Return the json representation of the records
    return jsonify(records)

if __name__ == "__main__":
    app.run(debug=True)