import json
import urllib.request
from data.getData import getData

# k = "http://api.wibbitz.com/clips/latest/?items=2000&orderedchannel=False&publisherid=92"
# webURL = urllib.request.urlopen(k)
# web = webURL.read().decode("utf-8")
# d = json.loads(web)
# t = set()
# articles = list(map(lambda x: x['title'], d))
# s = "http://www.haaretz.com/json/cmlink/7.1349843?vm=viewMode&pidx="
# ss = "&url=http%3A%2F%2Fwww.haaretz.com%2Fisrael-news&dataExtended=%7B%22contentId%22%3A%22%22%7D"
#
# for i in range(1,10):
#     webURL = urllib.request.urlopen(s+"%s"%i+ss)
#     web = webURL.read().decode("utf-8")
#     d = json.loads(web)
#     articles += list(map(lambda x:x['title'], d['items']))
#     print(i)
#
#
# for i in articles:
#     t.add(i)
#

# fk = open('haaretz.csv','r')
# f = open('haaretzMine.csv','r')
# t = set()
# a = f.read().split("\n")
# b = fk.read().split("\n")
#
# a = set(a+b)
# k = open("haaretzfinal.csv","w")
# k.write("\n".join(a))
import re
import time
testush = re.compile('font-size:16px;">(.+?)<')
a = []
k = [
{
    "domain": ".israelhayom.com",
    "expirationDate": 1561220273,
    "hostOnly": False,
    "httpOnly": False,
    "name": "__utma",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "196792756.3852388503.1498147202.1498147202.1498147202.1",
    "id": 1
},
{
    "domain": ".israelhayom.com",
    "expirationDate": 1498150073,
    "hostOnly": False,
    "httpOnly": False,
    "name": "__utmb",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "196792756.1.10.1498148273",
    "id": 2
},
{
    "domain": ".israelhayom.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "__utmc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "196792756",
    "id": 3
},
{
    "domain": ".israelhayom.com",
    "expirationDate": 1498148452,
    "hostOnly": False,
    "httpOnly": False,
    "name": "__utmt",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 4
},
{
    "domain": ".israelhayom.com",
    "expirationDate": 1513916273,
    "hostOnly": False,
    "httpOnly": False,
    "name": "__utmz",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "196792756.1498147202.1.1.utmcsr=israelhayom.co.il|utmccn=(referral)|utmcmd=referral|utmcct=/",
    "id": 5
},
{
    "domain": ".israelhayom.com",
    "expirationDate": 1498190401,
    "hostOnly": False,
    "httpOnly": False,
    "name": "rbzid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "dzJJOXdTc096cEN2aThZS1kxOEh4RTR4UVU1dTZaOEZudWlmOVBWOVEwaERWK1p5ZGs3Z0thSnJBN2ZtTmQ0TVhUcTBSaFJCdTRpTXIzNHZCKzRXV1FYaGswMG1LYjVmaVRSdk1BWUMwelJtY2V1b2NEcHJPZkpzUUZXOHh6YjVnWFZPNE5kVU5pMmV0MENxVHJHM082QmJLZWpPRFJnM0lhc0o5YVhQMGhFRmxrdU5scm5ERjF2Z2N3OExuODB3d3Z5anlBeDZCOGpOYmhQNFNPdnBMWWIrSmlkL01NNG1mRHpLblpLaU56dz1AQEAwQEBALTIyMjIyMjIyMDIw",
    "id": 6
},
{
    "domain": "www.israelhayom.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "PHPSESSID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "k3jsfmca55fp49ngjhhicefih6",
    "id": 7
},
{
    "domain": "www.israelhayom.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "TS0195b45d",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "01e361497cb2ec7cd96ebf67eea3a9ba01afd65add507b1c32a962999d50646fb3e784336cc396be59b59f491894e220014fe479a4",
    "id": 8
}
]
import requests
cookies = {a['name']:a['value'] for a in k}
for i in range(3171,3150,-1):
    print("http://www.israelhayom.com/site/today.php?id=%s"%i)
    webURL = requests.get("http://www.israelhayom.com/site/today.php?id=%s"%i, cookies=cookies)
    web = webURL.text
    m = re.findall(testush,web)
    if(len(m) == 0):
        print(web)
    print("found %s lines!"%(len(m)))
    for k in m:
        print(k)
        a.append(k)
    time.sleep(0.5)

f = open("ih.csv","w")
f.write("\n".join(a))


