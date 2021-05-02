import datetime
import time

import requests

URL = "https://api.vaksincovid.gov.my/az/?action=listppv"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'

while True:
    headers = {
        'User-Agent': USER_AGENT,
    }
    response = requests.get(URL, headers=headers)
    
    filename = datetime.datetime.now().isoformat() + ".json"
    with open(filename, "w") as f:
        f.write(response.text)

    print(filename)
    time.sleep(60)
