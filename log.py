import datetime
import time

import cloudscraper
import requests

URL = "https://api.vaksincovid.gov.my/az/?action=listppv"

headers = {
    'Referer': "https://www.vaksincovid.gov.my/",
    'Origin': "https://www.vaksincovid.gov.my",
}

scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'mobile': False,
            'platform': 'windows',
            }
        )

while True:
    try:
        response = scraper.get(URL, headers=headers)
    except:
        time.sleep(5)
        continue
    
    filename = datetime.datetime.now().isoformat() + ".json"
    with open(filename, "w") as f:
        f.write(response.text)

    print(filename)
    time.sleep(30)
