#!/usr/bin/python  
#coding=utf-8     
from xml.dom.minidom import parse  
import xml.dom.minidom

def KBPparser():
	infile = open('/home/john/entitylink/dataset/tac_kbp_2014(1).txt','w')
	#cur.execute("create table KBP2014(id int auto_increment primary key, docid varchar(50),mention varchar(100),candidate varchar(100))")
	DOMTree = xml.dom.minidom.parse("/home/john/entitylink/dataset/tac_2014_kbp_english_entity_linking_training_AMR_queries.xml")  
	Tree = DOMTree.documentElement
	data = Tree.getElementsByTagName('query')
	for item in data:
		#queryid = item.getAttribute('id')
		name = item.getElementsByTagName('name')[0].childNodes[0].data.encode('utf-8','ignore')
		name = '_'.join(name.split())
		wikititle = item.getElementsByTagName('wikititle')[0].childNodes[0].data.encode('utf-8','ignore')
		docid = item.getElementsByTagName('docid')[0].childNodes[0].data.encode('utf-8','ignore')
		print name,wikititle,docid
		#name = name.replace("'", "''")
		#wikititle = wikititle.replace("'", "''")
		strtemp = docid + '\t' + name + '\t' + wikititle + '\n'
		infile.write(strtemp)
if __name__ == '__main__':
	KBPparser()