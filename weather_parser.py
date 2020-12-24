from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://www.gismeteo.by/weather-minsk-4248/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    with webdriver.Chrome(r'C:\Users\Fezaru\Downloads\chromedriver.exe') as browser:
        browser.get(url)
        return browser.page_source


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    temp1 = soup.find('span', class_='js_value tab-weather__value_l')
    temp1 = temp1.get_text().strip()
    temp2 = soup.find('span', class_='tab-weather__feel-value')
    temp2 = temp2.find('span', class_='unit unit_temperature_c')
    temp2 = temp2.get_text().strip()
    print(temp1)
    print(temp2)


def parse():
    html = get_html(URL)
    get_content(html)


def get_temperatures():
    with webdriver.Chrome(r'C:\Users\Fezaru\Downloads\chromedriver.exe') as browser:
        browser.get(URL)
        html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')
    temp1 = soup.find('span', class_='js_value tab-weather__value_l')
    temp1 = temp1.get_text().strip()
    temp2 = soup.find('span', class_='tab-weather__feel-value')
    temp2 = temp2.find('span', class_='unit unit_temperature_c')
    temp2 = temp2.get_text().strip()
    return {'temp': temp1,
            'temp_feels': temp2}


if __name__ == '__main__':
    parse()
