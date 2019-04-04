"""
Created on 2019-04-04 @ 11:15

@author: Hackstreet Boys

        Script to set up backend server to receive form data and do processing on the data.
        
"""

from flask import Flask, request
from werkzeug.utils import secure_filename
import requests
from bs4 import BeautifulSoup
import re
import os
from ScrapeTwitter import getData

#url = 'https://twitter.com/Tesla'

app = Flask(__name__)

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print("got file")
        url = request.form['url']
        ans = getData(url)
        if ans:
            return f"""
            <img src="{ans[1]}">
            <br>
            <a href="{ans[0]}">Website link</a>
            <br>
            <p>{ans[2]}</p>
            """
        return "No information is given"

if __name__ == '__main__':
    app.run(debug = True)