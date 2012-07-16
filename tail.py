'''
Created on Jul 16, 2012

@author: epic2005

Example:
	tail(open(filepath, 'r'))
'''

import time

def tail(f):
    f.seek(0,2)
    while True:
        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue
        else:
            print line,