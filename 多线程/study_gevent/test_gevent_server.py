from gevent.server import StreamServer

def connect_handler(socket, address):
    for l in socket.makefile('r'):
        socket.sendall(l)

if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 8000), connect_handler)
    server.serve_forever()
