# Con esto vamos a poder travajar con URLs, pore ejemplo, HTTP

import urllib.request as requests

url = "https://docs.python.org/es/3/library/datetime.html"

with requests.urlopen(url) as response :
    html = response.read().decode()
    print(html)
