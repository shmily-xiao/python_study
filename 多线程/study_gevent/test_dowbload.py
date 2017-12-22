from gevent import monkey
monkey.patch_all()

import urllib2
from gevent.pool import Pool
import requests

def download(url):
    # return urllib2.urlopen(url).read()
    kwargs={}
    if kwargs.get('verify') == None:
        kwargs['verify'] = False
    if kwargs.get('timeout') == None:
        kwargs['timeout'] = 10
    if kwargs.get('allow_redirects') == None:
        kwargs['allow_redirects'] = False
    r = requests.request("GET", url, **kwargs)
    data = r.json()
    return data

if __name__ == '__main__':
    urls = ['https://10.143.160.250/lcx/scan/api/task/result/45245508-5a33-4199-b2f0-047388be7457'] * 20
    pool = Pool(2)
    print pool.map(download, urls)
