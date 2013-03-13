#! /usr/bin/env python
#coding=utf-8


import time
import re
import os

def tail(f):
    f.seek(0,2)
    while True:
        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue
        else:
            txt = line
            cat(line)


def cat(line):
    
    num = line.find('Deleted')

    if num > 0 :

        re1='.*?'
        re2='(?:[a-z][a-z0-9_]*)'
        re3='.*?'
        re4='(?:[a-z][a-z0-9_]*)'
        re5='.*?'
        re6='(?:[a-z][a-z0-9_]*)'
        re7='.*?'
        re8='(?:[a-z][a-z0-9_]*)'
        re9='.*?'
        re10='(?:[a-z][a-z0-9_]*)'
        re11='.*?'
        re12='((?:[a-z][a-z0-9_]*))'
        re13='.*?'
        re14='((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])'
        re15='.*?'
        re16='((?:[a-z][a-z]+))'
        re17='.*?'
        re18='((?:[a-z][a-z]+))'
        re19='.*?'
        re20='((?:\\/[\\w\\.\\-]+)+)'

        rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20,re.IGNORECASE|re.DOTALL)
        m = rg.search(line)

        if m:
            var1=m.group(1)
            ipaddress1=m.group(2)
            word1=m.group(3)
            word2=m.group(4)
            unixpath1=m.group(5)
            print "("+var1+")"+"("+ipaddress1+")"+"("+word1+")"+"("+word2+")"+"("+unixpath1+")"

    
            fp = os.popen("rsync -vzrt --delete-excluded=" + unixpath1 + " /filepath/" + var1 + " dst_ip::" + var1 + " --password-file=/etc/rsyncd.password",'r')
            msg = fp.read()
            print msg

if __name__ == '__main__':
    f = open("/var/log/ftpd.log", 'r')
    tail(f)
