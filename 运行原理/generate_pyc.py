import imp

import sys

def generate_pyc(name):

    fp, pathname, description = imp.find_module(name)

    try:
        imp.load_module(name, fp, pathname, description)
    finally:
        if fp:
            fp.close()


if __name__ == '__main__':
    print sys.argv
    generate_pyc("demo")
    # generate_pyc(sys.argv[1])