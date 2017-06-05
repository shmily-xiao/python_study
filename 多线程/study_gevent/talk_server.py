#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent
from gevent.queue import Queue
from gevent.server import StreamServer

users = {'www','xxx'} # mapping of username -> Queue


def broadcast(msg):
    msg = msg + '\n'
    for v in users.values():
        v.put(msg)


def reader(username, f):
    for l in f:
        msg = "%s > %s" %(username, l.strip())
        broadcast(msg)

def writer(q, sock):
    while True:
        msg = q.get()
        sock.sendall(msg)


def read_name(f, sock):
    while True:
        sock.sendall('Please enter your name: ')
        name = f.readline().strip()
        if name:
            if name in users:
                sock.sendall('That username is already taken. \n')
            else:
                return name


def handle(sock, client_addr):
    f = sock.makefile()
    name = read_name(f, sock)
    broadcast('## %s joined from %s.'%(name, client_addr[0]))

    q = Queue()
    users[name] = q

    try:
        r = gevent.spawn(reader, name, f)
        w = gevent.spawn(writer, q, sock)
        gevent.joinall([r, w])
    finally:
        del(users[name])
        broadcast('## %s left the chatt.'% name)


def start_beer_request():
    http.get('/api/beer', handle_response)


def handle_response(resp):
    beer = load_beer(resp.json)
    do_something(beer)


# 闭包方式
def get_fruit(beer_id, callback):
    def handle_response(resp):
        beer = loac_beer(resp.json)
        callback(beer)
    http.get('/api/beer/%d' % beer_id, handle_response)



if __name__ == '__main__':
    import sys
    try:
        myip = sys.argv[1]
    except IndexError:
        myip = '0.0.0.0'
    print 'To join, telnet %s 8001' % myip
    s = StreamServer((myip, 8001), handle)
    s.serve_forever()

