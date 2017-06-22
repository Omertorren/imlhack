import json
import urllib.request
from data.getData import getData

# k = "http://api.wibbitz.com/clips/latest/?items=2000&orderedchannel=false&publisherid=92"
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

fk = open('haaretz.csv','r')
f = open('haaretzMine.csv','r')
t = set()
a = f.read().split("\n")
b = fk.read().split("\n")

a = set(a+b)
k = open("haaretzfinal.csv","w")
k.write("\n".join(a))

