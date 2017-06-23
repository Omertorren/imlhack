import dill as pickle

# print(s)
def haaretzValidator():
    import json
    import urllib.request
    import base64
    k = base64.standard_b64decode(
        b'aHR0cDovL2FwaS53aWJiaXR6LmNvbS9jbGlwcy9sYXRlc3QvP2l0ZW1zPTIwMDAmb3JkZXJlZGNoYW5uZWw9ZmFsc2UmcHVibGlzaGVyaWQ9OTI=')
    s = base64.standard_b64decode(
        b'aHR0cDovL3d3dy5oYWFyZXR6LmNvbS9qc29uL2NtbGluay83LjEzNDk4NDM/dm09dmlld01vZGUmcGlkeD0=')
    ss = base64.standard_b64decode(
        b'JnVybD1odHRwJTNBJTJGJTJGd3d3LmhhYXJldHouY29tJTJGaXNyYWVsLW5ld3MmZGF0YUV4dGVuZGVkPSU3QiUyMmNvbnRlbnRJZCUyMiUzQSUyMiUyMiU3RA==')
    k=k.decode('utf-8')
    s=s.decode('utf-8')
    ss=ss.decode('utf-8')
    webURL = urllib.request.urlopen(k)
    web = webURL.read().decode("utf-8")
    d = json.loads(web)
    t = set()
    articles = list(map(lambda x: x['title'], d))

    for i in range(1,10):
        webURL = urllib.request.urlopen(s+"%s"%i+ss)
        web = webURL.read().decode("utf-8")
        d = json.loads(web)
        articles += list(map(lambda x:x['title'], d['items']))

    for i in articles:
        t.add(i)
    return t

f = open("fmdl.pkl","wb")
pickle.dump(haaretzValidator,f)
