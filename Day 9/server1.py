#flask server

from flask import Flask
from logger import trigger_log_save
from scrape import run as scrape_runner

app = Flask (__name__)

@app.route("/", methods = ['GET'])
def hello_world():
    #run some other code here
    return 'Hello, world. This is Flask'


# http://localhost:8000/abc
@app.route("/abc", methods = ['GET'])
def abc_view():
    #run some other code here
    return 'Hello, world. This is abc'


@app.route("/box-office-mojo-scraper", methods = ['POST'])
def box_office_scraper_view():
    #run some other code here
    trigger_log_save()
    scrape_runner()
    return {'data': [1,2,3]}