import os
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Database setup
path = "data/portland.sqlite"
engine = create_engine(f"sqlite:///{path}")

# Reflect existing database ito a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to tables
Restaurants = Base.classes.restaurants

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods = ["GET"])
def search():
    try:
        if request.method == "GET":
            session = Session(engine)
            results = session.query(Restaurants.name, Restaurants.categories).all()
            session.close()
            restaurant_list = []
            for name, categories in results:
                restaurant_dict = {}
                restaurant_dict['name'] = name
                restaurant_dict['categories'] = categories



            name = request.args.get("name")
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            query = "SELECT * from restaurants WHERE categories = vietnamese"
            result = cursor.execute(query)
            result = result.fetchall()[0][0]
            return render_template("index.html", restaurants = result)
    except:
        return render_template("index.html", restaurants = "")

if __name__ == "__main__":
    app.run(debug=True)