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
import scrape
import uuid

#url = 'https://twitter.com/Tesla'

app = Flask(__name__)

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        try:
            f = request.files['file']
            if '.csv' not in f.filename:
                filename = None
            else:
                filename = str(uuid.uuid4())
                f.save(secure_filename(filename))
        except:
            filename = None
        url_list = request.form['url']
        ld = request.form['ld']
        rtype = request.form['rtype']
        r_file = data_process.input_process(rtype = rtype, csv = filename, text = url_list, ld = ld)
        send_file(r_file)
        logo = scrape.get_twitter_logo(url_list)
        desc = scrape.get_twitter_desc(url_list)
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