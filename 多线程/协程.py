# from bs4 import Beautifulsoup
import requests
import gevent
from gevent import monkey, pool
monkey.patch_all()
jobs = []
links = []
p = pool.Pool(10)
urls = [
    'http://www.google.com'
]
def get_links(url):
    r = requests.get(url)
    if r.status_code == 200:
        print r.text
        # soup = Beautifulsoup(r.text)
        # links + soup.find_all('a')

for url in urls:
    jobs.append(p.spawn(get_links, url))

gevent.joinall(jobs)