from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import username
from config import passwd

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<username>:<passwd>@localhost:5432/restaurant_db"
db = SQLAlchemy(app)

class Biz(db.Model):
    __tablename__="yelp_data"
    id=db.Column(db.Serial, primary_key=True)
    name=db.Column(db.Text)
	address=db.Column(db.Text)
	city=db.Column(db.Text)
	state=db.Column(db.Text)
	postal_code=db.Column(db.Text)
	latitude=db.Column(db.Decimal)
	longitude=db.Column(db.Decimal)
	stars=db.Column(db.Decimal)
	review_count=db.Column(db.Integer)
	categories=db.Column(db.Text)

    def __init__(self, name, address, city, state, postal_code, latitude, longitude, stars, review_count, categories):
        self.name=name
        self.address=address
        self.city=city
        self.state=state
        self.postal_code=postal_code
        self.latitude=latitude
        self.longitude=longitude
        self.stars=stars
        self.review_count=review_count
        self.categories=categories

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["GET", "POST"])
    if request.method == "GET":
        results = db.session.query(Biz).filter(Biz.id == 1)
        for result in results:
            print(result.name)

    return render_template("success.html", data=name)

if __name__ == "__main__":
    app.run(debug=True)