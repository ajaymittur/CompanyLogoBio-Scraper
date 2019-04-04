"""
Created on Thur Apr  4 11:00:41 2019

@author: Hackstreet Boys

        Script to extract company logo, description and website from Twitter
        Given the url, returns the [company_url, logo_url & company_desc]
        
"""

import requests
from bs4 import BeautifulSoup

def getData(url):
        response = requests.get(url)
        logo_soup = BeautifulSoup(response.text, 'html.parser')

        company_url_tags = logo_soup.find_all('a', attrs={'class': 'u-textUserColor', 'target': '_blank'})
        company_url_tag = company_url_tags[0]
        company_url = company_url_tag['href']
        company_url

        logos_tags = logo_soup.find_all('img', class_='ProfileAvatar-image')
        logo_tag = logos_tags[0]
        logo_url = logo_tag['src']
        logo_url

        response = requests.get(company_url)
        desc_soup = BeautifulSoup(response.text, 'html.parser')

        description_tags = desc_soup.find_all('meta', attrs={'property': 'og:description'})
        description_tag = description_tags[0]
        company_desc = description_tag['content']
        company_desc

        print ("Company Website: ", company_url )
        print ("Logo URL: ", logo_url)
        print ("Company Description: ", company_desc)

        return [company_url, logo_url, company_desc]
