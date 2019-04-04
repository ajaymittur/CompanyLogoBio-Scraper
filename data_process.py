"""
Created on Thu Apr  4 12:26:53 2019

@author: Hackstreet Boys

    Script to perform file conversion
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import scrape
import uuid

def get_csv_df(file):
    return pd.read_csv(file, header=None)

def get_string_df(string):
    return pd.DataFrame(string.split())

def concat_df(csv,string):
    return csv.append(string, ignore_index=True)

def return_csv(df):
    filename = str(uuid.uuid4())
    df.to_csv(filename)
    return filename

def return_json(df):
    filename = str(uuid.uuid4())
    df.to_json(filename)
    return filename

def input_process(**params):
    """
    Form input processing and file conversion.
    Parameters:
    file : csv file location string. May be None.
    text : text string containing all URLs. May be None.
    ld = specifies logo or description. Logo by default. Option between 'l' or ' d'
    type : return type, .csv by default. Option between 'csv' and 'json'
    """
    if params['file'] and params['text']:
        df = concat_df(params['file'],params['text'])
    elif params['file']:
        df = get_csv_df(params['file'])
    elif params['text']:
        df = get_string_df(params['text'])
    else:
        if params['rtype'] == 'json':
            return 'invalid.json'
        else:
            return 'invalid.csv'

    if params['rtype'] == 'json':
        return return_json(scrape.return_scraped_df(df, params['ld']))
    
    return return_csv(scrape.return_scraped_df(df))




        