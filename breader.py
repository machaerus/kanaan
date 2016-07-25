#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import re
import os
import copy
import sys
#from sage.all import *
import sage.all


##################################################

def main():

	print """
+-------------------------------+
|  *** Bible Permuter v0.3 ***  |
+-------------------------------+
	"""

	filename = sys.argv[1]

	try:
		fin = open(filename, 'r')
		print "* Reading file: ", fin.name, " \n"
	except IOError:
		print "* Cannot open file: "
		print "* %s \n" % filename

	text = fin.read()
	fin.close()

	text = tokenize(text)

	length = len(text)
	perms = sage.all.factorial(length).n(digits=2)

	print "*** Original text ***"
	#print text
	print "Words (total): %d" % length
	print "Total permutations possible: %s" % str(perms)

	print ""
	print "%9s %12s %12s %15s %15s" % ("Computed", "Total", "Percent", "Time elapsed", "Est. time left")

	QuickPerm(1, text, length, perms)

	# for permutation in res:
	# 	for word in permutation:
	# 		print(word),
	# 	print "\n"
	# 	sleep (0.0005)

##################################################

def tokenize(text):
	return re.findall(r'\w+', text)

##################################################

def join(list):
	text = ""
	for word in list:
		text = text + word + " "
	return text

##################################################

def QuickPerm(num, text, length, perms):
	results = []
	p = []
	iteration = 0
	start = time.time()
	#print start
	p = [0]*length
	i, j = 0, 0
	results.append(copy.deepcopy(text))
	i = 1
	while i < length :
		
		time.sleep (0.0002)
		if p[i] < i :

			#--display stats--------
			#-----------------------

			iteration += 1 	# number of current program iteration
			num += 1 		# number of total iterations computed
			curr_time = time.time()-start
			percent = (iteration/perms*100).n(digits=1)
			perms_per_s = iteration/curr_time
			# estimated time left in seconds
			time_left = (perms-iteration)/perms_per_s
			#hours_left = (time_left/360).n(digits=1)
			#days_left = (time_left/8640).n(digits=1)
			years_left = (time_left/3153600).n(digits=1)
			sys.stdout.write('\r%9s %12s %12s%% %13ss %15s years' % (iteration, perms, percent, str(round(curr_time,1)), years_left ))
			sys.stdout.flush()

			#-----------------------

			j = i % 2 * p[i]
			tmp = text[j]
			text[j] = text[i]
			text[i] = tmp
			# save the permutation found:

			if iteration % 100000 == 0 :
				try:
					fout = open("permutations/"+str(num)+".bibl",'w')
					for word in text :
						fout.write(word+" ")
					fout.close()
				except IOError:
					print "* Cannot create file!"

			#results.append(copy.deepcopy(text))
			p[i] += 1
			i = 1
		else:
			p[i] = 0
			i += 1
	stop = time.time()
	#print stop
	print "\n"
	print "Task completed successfully."
	print "Total time: %ds. \n" % (stop - start)
	#print "Permutations per second: %s" % perms*1/(stop - start)
	return results

##################################################

if __name__ == '__main__': main()