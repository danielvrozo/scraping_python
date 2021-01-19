import bancopopular
from flask import Flask, render_template
import os
import sys


app = Flask(__name__)

@app.route('/bancopopular')
def index():
    return bancopopular.app()
    
@app.route('/bancolombia')
def bancolombia():
    return 'bancolombia'
    
if __name__ == '__main__': app.run(debug=True)

