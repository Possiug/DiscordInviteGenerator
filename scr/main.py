import requests
import random
import string
import time
import json
import os.path
from threading import Thread
from bs4 import BeautifulSoup as bs

DB = []
API = "https://discordapp.com/api/v7/invite/"
dbPath = 'db.json'

proxy = {
    'https':'http://161.117.81.228:483'
}

if(os.path.exists(dbPath)):
    with open(dbPath, 'r+') as db:
        try:
            loadedJs = json.load(db)
            DB = loadedJs
            print("db was loaded!")
            #print(DB)
        except Exception as err:
            print("error while reading file!: ",err)
            exit()
else:
    print("db doesn't exist, recreating file!")
    with open(dbPath, 'w') as db:
        json.dump(DB, db, indent=4)

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

def check(invite_str):
    link = API + invite_str
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    r = None
    try:
        r = requests.get(link, headers=headers,proxies=proxy)
    except Exception as err:
        print(err)
    r = str(r)
    #print(r)
    if "404" in r:
        print("no")
    elif "200" in r:
        print("yes " + invite_str)
        save(invite_str)
    elif "429" in r:
        print("rate-limit!")
        time.sleep(25)

def generation(a) :
    invite = []

    for i in range(0,a):
        choice = random.randint(0,1)

        if choice == 0 :
            invite.append(random.randint(0,9))
        
        elif choice == 1 :
            invite.append(random.choice(string.ascii_letters))
    
    invite_str = ''.join(str(e) for e in invite)
    print(invite_str)

def save(str):
    if(checkRepeat(str)):
        return
    DB.append(str)
    with open(dbPath, "w") as f:
        json.dump(DB,f, indent=4)

    

def checkRepeat(str):
    for val in DB:
        if(val == str):
            return val
    return False

def main():
    while(True):
        choice = random.randint(-1,1)
        randTimeOut = random.random()
        timeOut = 1.8 + choice * randTimeOut
        #print(timeOut)
        time.sleep(timeOut)
        check(str(generation(8)))

Theards =[]


for i in range(1):
    a = Theards.__len__()
    Theards.append(Thread(target=main,daemon=True))
    Theards[a].start()

while(True):
    try:
        input()
    except KeyboardInterrupt:
        exit()




        