#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import random
import sys
import copy
import math

def main():

	print """
+-------------------------------+
|    ***   Kanaan v0.1   ***    |
+-------------------------------+

Create your very own promised land!
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

	res = randomPerm(text)

	permutation = []
	for i in xrange(0, len(text)-1) :
		r = res[i]
		permutation.append(text[r])

	try:
		fout = open("kanaan.bibl",'w')
		for word in permutation :
			fout.write(str(word)+" ")
		fout.close()
	except IOError:
		print "* Cannot create file!"

	gem_value = 0
	i = 0
	for word in permutation :
		i += 1
		gem_value += gematric(word) ** int(math.floor(math.sqrt(i)))
		gem_value = gem_value % 2147483647

	#print len(permutation)
	#print join(begin)
	print "Your gematric minecraft seed is: %d \n" % gem_value


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

def uniform(m) :
	rand = random.randint(0,m)
	return rand

##################################################

def randomPerm(text) :
	res = copy.deepcopy(text)
	for i in xrange(0,len(res)-1) :
		j = uniform(i)
		res[i] = res[j]
		res[j] = i
	return res

##################################################

def gematric(word) :
	def value(letter) :
		value = {
			'a' : 1,
			'A' : 1,
			'B' : 2,
			'b'	: 2,
			'C' : 3,
			'c'	: 3,
			'D' : 4,
			'd'	: 4,
			'E' : 5,
			'e'	: 5,
			'F' : 6,
			'f'	: 6,
			'G' : 7,
			'g'	: 7,
			'H' : 8,
			'h'	: 8,
			'I' : 9,
			'i'	: 9,
			'K' : 10,
			'k'	: 10,
			'L' : 20,
			'l'	: 20,
			'M' : 30,
			'm'	: 30,
			'N' : 40,
			'n'	: 40,
			'O' : 50,
			'o'	: 50,
			'P' : 60,
			'p'	: 60,
			'Q' : 70,
			'q'	: 70,
			'R' : 80,
			'r'	: 80,
			'S' : 90,
			's'	: 90,
			'T' : 100,
			't'	: 100,
			'U' : 200,
			'u'	: 200,
			'X' : 300,
			'x'	: 300,
			'Y' : 400,
			'y'	: 400,
			'Z' : 500,
			'z'	: 500,
			'J' : 600,
			'j'	: 600,
			'V' : 700,
			'v'	: 700,
			'W' : 900,
			'w'	: 900
		}

		if str.isalpha(letter) :
			return value[letter]
		else :
			return 0

	sum = 0
	for letter in word :
		sum += value(letter)

	return sum

##################################################



##################################################

if __name__ == '__main__': main()