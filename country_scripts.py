import os
import re

class Dirty:
	def clean_up_list(self, fname):
		fobj = open(fname, 'r')
		temp = open('tmp.txt', 'a')
		lines = fobj.readlines()
		for line in lines:
			if line.strip() == "":
				continue
			temp.write(line.split()[0] + '\n')
		temp.close()
		fobj.close()
		open(fname, 'w').close()
		fobj = open(fname, 'a')
		lines = open('tmp.txt', 'r').readlines()
		for line in lines:
			#print line
			fobj.write(line)
		fobj.close()
		os.remove('tmp.txt')

	def generate_go(self, c_list, c_code):
		countries = open(c_list, 'r').readlines()
		codes = open(c_code, 'r').readlines()
		for country in countries:
			c = re.sub('[^0-9a-zA-Z\n]+', '_', country.upper())
			if c in codes:
				print 'pb.CountryCode_' + c.strip()


