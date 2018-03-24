# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:01:09 2018

@author: arthu
"""

from flask import Flask,  render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
    
