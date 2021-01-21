from bancopopular import scraping
from flask import Flask
import os
import sys

app = Flask(__name__)
if __name__ == '__main__': app.run()
    
@app.route("/bancopopular")
def popular():
    scraping_web = scraping()
    return scraping_web
    

@app.route('/bancolombia')
def bancolombia():
    return 'bancolombia'

