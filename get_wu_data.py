
# script to scrape rainfall data from Weather Underground's almanac
# e.g. http://api.wunderground.com/api/c45081a756a6dc05/history_20060405/q/CA/San_Francisco.json


from json import loads
from urllib2 import urlopen
from datetime import datetime, timedelta

def download_json(url):
    weather = urlopen(url)
    string = weather.read()
    weather.close()
    return loads(string)

d, x, y = [], [], []
x1 = 0.0
key = "c45081a756a6dc05"

for day in range(1):
    url = ''.join(['http://api.wunderground.com/api/', key,
    '/history_20100405',
    # (20100405).strftime('%Y%m%d'),
    '/q/NE/Whiteclay.json'])
    data = download_json(url)
    for k in data['history']['observations']:
        y0 = float(k['precipm'])
        print y0
        if y0 < 0.0:
            continue
        else:
            x.append(x1 + float(k['date']['hour'] )+
            round((float(k['date']['min'] ) /60.0) ,2))
            y.append(y0)
    x1 += 24.0
