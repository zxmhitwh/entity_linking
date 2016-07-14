#coding=utf-8
import urllib
import re

infile = open("/home/john/entitylink/dataset/page-links_en.nt")
outfile = open('/home/john/entitylink/dataset/page-links_en.txt', 'w')
line = infile.readline()
num = 0
while line:
	num += 1
	if '#' in line or '<http://dbpedia.org/resource//' in line or '<http://dbpedia.org/resource/.' in line:
		pass
	else:
		a,b = line.strip('<http://dbpedia.org/resource/').strip('> .\n').split('> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/')
		entity1 = urllib.unquote(a).decode('utf-8','ignore').encode('utf-8')
		entity2 = urllib.unquote(b).decode('utf-8','ignore').encode('utf-8')
		strtemp = entity1 + '\t' + entity2 + '\n'
		print str(num) + ' ' + strtemp
		outfile.write(strtemp)
	line = infile.readline()