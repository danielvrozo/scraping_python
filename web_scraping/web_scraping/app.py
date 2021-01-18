
from flask import Flask, render
import os
import sys


app = Flask(__name__)

@app.route('/bancopopular')
def app():
    return bancopopular.app()
    
@app.route('/bancolombia')
def bancolombia():
    return 'bancolombia'
    
if __name__ == '__main__': app.run(debug=True)

