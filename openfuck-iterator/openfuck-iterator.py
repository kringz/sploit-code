#!/usr/bin/python

from subprocess import call

#hex(version)

for i in xrange(137):
	form = "0x{:02x}".format(i)
	print form
#	call(["./OpenFuck", i, "192.168.15.244", "8000"])
