from bs4 import BeautifulSoup
import requests

URL = """
    https://in.finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAKT4WErrMRBC2ioKGWo0-u-cukw2sDtMtGnog672ta-C2jEld5qHJRUi3Du4PQyYeGJHcltWNgjKgQal_qvHJgAce5ZLI3tS5jwIezUSqrHxWc3AMf6IwMV0TGAayZanzMSSp-2YgalHKC9UuGsvX1pzVrHApXSLtNhS62N8Q9y0
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

sensex_value_text = soup.find(
    "span", {"class": "Trsdu(0.3s) Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)"}).text
sensex_value = float(sensex_value_text.replace(",", ""))

target_value = 51000

print(sensex_value)
