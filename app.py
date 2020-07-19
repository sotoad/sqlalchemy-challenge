# Python SQL toolkit, Object Relational Mapper and others
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import numpy as np
import datetime as dt

#create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    return(
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"


@app.route("/api/v1.0/precipitation")
def precipitation():
    precip_scores = (session.query(Measurement.date, Measurement.prcp)
        .filter(Measurement.date <='2017-08-23')
        .filter(Measurement.date >= '2016-08-23')
        .order_by(Measurement.date).all())

    precipitationlist = []
        for scores in precip_scores:
            prcpdict = {scores.date: scores.prcp}
            precipitationlist.append(prcpdict)

        return jsonify(precipitationlist)


@app.route("/api/v1.0/stations")
def stations():
    names = session.query(Station.name).all()
    station_names = list(np.ravel(names))
    return jsonify(station_names)



















if__name__="__main__"
app.run(debug=True)