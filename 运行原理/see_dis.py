import dis


s = open('demo.py').read()
co = compile(s, 'demo.py', 'exec')

dis.dis(co)