#!/usr/bin/env python

import pexpect
import sys
import os
import re

os.chdir("/home/admin/TestON/bin")
print os.popen("pwd").read()
child = pexpect.spawn("./cli.py")
child.expect("Solutions")
child.expect("teston>")
response = child.before + child.after
if re.search("teston>",response):
    print "TestON is running"
else:
    print "TestON not running"
    sys.exit()
child.sendline("run "+str(sys.argv[1]))
child.expect("CASE\sINIT",timeout=120)
print child.before + child.after
while 1:
    #i = child.expect("Test\sExecution\sSummary",timeout=3600)
    #if i == 1:
    #    break
    #elif i == 0:
    #    break
    i = child.expect("Result\ssummary\sfor", timeout=1800)
    if i == 0:
        print child.before+child.after
    else: 
        break
    
    #else:
    #    print child.before+child.after
print child.before+child.after
print child.before
child.sendline("quit")
