"""
Created on Thur Apr  4 11:00:41 2019

@author: Hackstreet Boys

        Script to extract company logo, description and website from Twitter
        Given the url, returns the [company_url, logo_url & company_desc]
        
"""

import requests
from bs4 import BeautifulSoup
import tldextract

def get_company_logo(url):
    url_extract = tldextract.extract(url)
    domain_name = url_extract.domain + '.' + url_extract.suffix
    return f'http://logo.clearbit.com/{domain_name}'

def get_twitter_logo(url):
    response = requests.get(url)
    logo_soup = BeautifulSoup(response.text, 'html.parser')
    logos_tags = logo_soup.find_all('img', class_='ProfileAvatar-image')
    logo_tag = logos_tags[0]
    logo_url = logo_tag['src']
    return logo_url

def get_company_desc(url):
    response = requests.get(url)
    desc_soup = BeautifulSoup(response.text, 'html.parser')
    description_tags = desc_soup.find_all('meta', attrs={'property': 'og:description'})
    description_tag = description_tags[0]
    company_desc = description_tag['content']
    return company_desc

def get_twitter_desc(url):
    response = requests.get(url)
    logo_soup = BeautifulSoup(response.text, 'html.parser')
    description_tags = desc_soup.find_all('meta', attrs={'property': 'og:description'})
    description_tag = description_tags[0]
    company_desc = description_tag['content']
    return company_desc

def get_logo(url):
    if 'twitter.com' in url:
        return get_twitter_logo(url)
    else:
        return get_company_logo(url)


def get_desc(url):
    if 'twitter.com' in url:
        return get_twitter_desc(url)
    else:
        return get_company_desc(url)

def return_scraped_df(**val):
    print(val['df'])
    if val['ld'] == None:
        val['ld'] = 'l'
    if val['ld'] == 'l':
        val['df'].columns = ['url']
        val['df']['logo'] = val['df']['url'].apply(get_logo)
        return val['df']
    else:
        val['df'].columns = ['url']
        val['df']['desc'] = val['df']['url'].apply(get_desc)
        return val['df']

