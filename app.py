from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    return "<p>Climbing App</p>"