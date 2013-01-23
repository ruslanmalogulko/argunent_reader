#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import logging
import datetime

print(sys.argv)
arg = sys.argv

file = open('/home/russel/DEV/py/argument_reader/log.txt', 'a')
y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
h = datetime.datetime.now().hour
min = datetime.datetime.now().minute

full_time = [y, m, d, h, min]

help = 'help'
if len(arg) != 1:
	print "This is help part of program" 

	file.write('%s.%s.%s   %s:%s\n' % (y, m, d, h, min))
	iter = 1
	for item in arg[1:]:
		file.write('argument %d: %s\n' %(iter, item))
		iter+=1
	file.write('\n')



file.close()