#!/usr/bin/python

from subprocess import call

# openf loop script
# Stephen Krings


for i in xrange(138):
	form = "0x{:02x}".format(i)
	call(["./OpenF", form, "192.168.15.244", "8000"])
