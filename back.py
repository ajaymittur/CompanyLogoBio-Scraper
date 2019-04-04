"""
Created on 2019-04-04 @ 11:15

@author: Hackstreet Boys

        Script to set up backend server to receive form data and do processing on the data.
        
"""

from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import requests
from bs4 import BeautifulSoup
import re
import os
import scrape
import uuid
import data_process
import pandas as pd
#url = 'https://twitter.com/Tesla'

app = Flask(__name__)
UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/result', methods = ['GET', 'POST'])
def result():
    try:
        f = request.files['file']
        filename = str(uuid.uuid4()) + '.csv'
        f.save(secure_filename(filename))
    except:
        filename = None
    try:
        url_list = request.form['url']
    except:
        url_list = None
    ld = request.form['ld']
    rtype = request.form['rtype']
    r_file = data_process.input_process(rtype = rtype, file = filename, text = url_list, ld = ld)
    if filename != None:
        os.remove(filename)
    return send_file(r_file)

if __name__ == '__main__':
    app.run(debug = True)