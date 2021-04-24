from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars"
mongo = PyMongo(app)


mongo = PyMongo(app, uri="mongodb://localhost:27017/app_name")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # # Find one record of data from the mongo database
     mission_to_mars = mongo.db.mission_to_mars.find_one()

    # # Return template and data
    return render_template("index.html", mission_to_mars=mission_to_mars)
    


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
  
    # Run scrapped functions
    mission_to_mars = mongo.db.mission_to_mars
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_f = scrape_mars.scrape_mars_facts()
    mars_w = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    # use mongo update to upsert data
    
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
