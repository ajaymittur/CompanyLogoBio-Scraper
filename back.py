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
import ScrapeTwitter

#url = 'https://twitter.com/Tesla'

app = Flask(__name__)

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print("got file")
        url = request.form['url']
        logo = ScrapeTwitter.get_twitter_logo(url)
        desc = ScrapeTwitter.get_twitter_desc(url)
        if logo and desc:
            return f"""
            <img src="{logo}">
            <br>
            <a href="{desc[0]}">Website link</a>
            <br>
            <p>{desc[1]}</p>
            """
        return "No information is given"

if __name__ == '__main__':
    app.run(debug = True)