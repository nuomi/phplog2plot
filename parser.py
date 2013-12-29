#!/usr/bin/env python

#TODO  http://matplotlib.org/examples/api/date_demo.html
import re

regex = re.compile(".*WARNING\:\s\[pool\s.*")
regex_busy = re.compile(".*busy.*servers\)")
regex_slow = re.compile(".*too\sslow")
regex_timeout = re.compile(".*timed\sout")
regex_exit = re.compile(".*exited\son\ssignal")
regex_reach = re.compile(".*reached\s.*setting")
regex_insufficient_disk_space = re.compile(".*Insuf.*space")


fd = open('php5-fpm-warn.log')
rt = open('php5-fpm-warn-parse.log', 'w')
content = fd.readline()

def save2busy_dict():
	pass
def save2slow_dict():
	pass
def save2timeout_dict():
	pass
def save2exit_dict():
	pass
def save2reach_dict():
	pass
def save2space_dict():
	pass

def write_to_file(reg_rt):
	line = reg_rt[0]+'\n'
	line = re.sub("child\s\d*", "", line)
	#TODO datetime.datetime.strptime("05-Oct-2013 11:10:19", "%d-%b-%Y %H:%M:%S")
	rt.write(line)	

while (content != ""):
	if not regex.search(content):
		continue
	#test 'seems busy'
	ret = regex_busy.findall(content)
	if ret:
		write_to_file(ret)
		content = fd.readline()
		continue

	#test slow script
	ret = regex_slow.findall(content)
	if ret:
		write_to_file(ret)
		content = fd.readline()
		continue

	#test timeout
	ret = regex_timeout.findall(content)
	if ret:
		write_to_file(ret)
		content = fd.readline()
		continue

	ret = regex_reach.findall(content)
	if ret:
		write_to_file(ret)
		content = fd.readline()
		continue

	ret = regex_insufficient_disk_space.findall(content)
	if ret:
		write_to_file(ret)
		content = fd.readline()
		continue

	ret = regex_exit.findall(content)
	if ret:
		content = fd.readline()
		continue
		
	write_to_file(content)
	content = fd.readline()

rt.close()
