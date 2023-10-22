from bs4 import BeautifulSoup as bs
import requests
import time


def getProxies():
    soup = bs(requests.get('https://free-proxy-list.net/').content, "html.parser")
    for element in soup.find("table").find_all("tr"):
        tds = element.find_all("td")
        try:
            host = tds[0].text.strip()
            port = tds[1].text.strip()
            https = tds[6].text.strip()
        except IndexError:
            continue
        allProxies = []
        if https == "yes":
            try:
                proxy = {'https':f'http://{host}:{port}'}
                requests.get('https://google.com',proxies=proxy,timeout=1)
                allProxies.append(f"{host}:{port}")
                print(f"{host}:{port}")
            except Exception as err:
                continue
        return allProxies