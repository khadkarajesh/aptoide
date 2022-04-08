import logging

import requests
from bs4 import BeautifulSoup

from app_info import AppInformation

APP_NAME_CSS_CLASS = "header-touch__AppName-sc-1om5ik5-5"
APP_VERSION_CSS_CLASS = "mini-versions__LatestVersion-sc-19sko2j-5"
APP_NUMBER_OF_DOWNLOADS_CSS_CLASS = "mini-stats__Info-sc-188veh1-6"
APP_RELEASE_DATE_CSS_CLASS = "mini-versions__VersionDate-sc-19sko2j-6"
APP_DESCRIPTION_CSS_CLASS = "description__Paragraph-sc-45j1b1-1"


class ApiService:
    def __init__(self, url):
        self.url = url

    def search(self) -> AppInformation:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            name = soup.find('h1').text
            version = soup.find_all('div', attrs={'class': APP_VERSION_CSS_CLASS})[0].text
            download_count = soup.find_all('span', attrs={'class': APP_NUMBER_OF_DOWNLOADS_CSS_CLASS})[0].text
            release_date = soup.find_all('div', attrs={'class': APP_RELEASE_DATE_CSS_CLASS})[0].text.strip("()")
            description = soup.find_all('p', attrs={'class': APP_DESCRIPTION_CSS_CLASS})[0].text
            return AppInformation(name=name,
                                  version=version,
                                  download=download_count,
                                  release_date=release_date,
                                  description=description)
        except IndexError as e:
            logging.error(f"Couldn't find the html element with class name {e}")
