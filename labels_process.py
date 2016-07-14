#coding=utf-8
import urllib
import re

infile = open("/home/john/entitylink/dataset/labels_en.nt")
outfile = open('/home/john/entitylink/dataset/labels_en.txt', 'w')
line = infile.readline()
num = 0
while line:
	match = re.search("(<http://dbpedia.org/resource/)(.*)(> <http://www.w3.org/2000/01/rdf-schema#label>)",line)
	if match:
		entity = match.group(2)
		entity1 = urllib.unquote(entity).decode('utf-8','ignore').encode('utf-8')
		strtemp = entity1 + '\t' + entity1 + '\n'
		outfile.write(strtemp)
		print str(num) + ' ' + strtemp
		num += 1
	line = infile.readline()