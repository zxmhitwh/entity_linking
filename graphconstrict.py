#coding=utf8
import MySQLdb

def getPath(entitypair,routelen):
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	if routelen == 2:
		mysql = "select a.entityname,a.linkname,b.linkname from pagelinks as a join pagelinks as b where a.entityname = \""+entitypair[0]+"\" and b.linkname = \""+entitypair[1]+"\" and a.linkname = b.entityname"
		cur.execute(mysql)
		resultlist = cur.fetchall()
		for eachresult in resultlist:
			print eachresult
	#if len = 1:
	
def getPair(entityset):
	pair = []
	for entity1 in entityset.keys():
		for entity2 in entityset.keys():
			if entity1 != entity2:
				for each1 in entityset[entity1]:
					for each2 in entityset[entity2]:
						pair.append([each1,each2])
	return pair

def getCandidateset(mentionset):
	mentiondic = {}
	for mention in mentionset:
		temparray = getCanByEdit(mention,3)
		mentiondic[mention] = temparray
	return mentiondic

if __name__ == '__main__':
	getPath(['Michael_Jordan','Chicago_Bulls'],2)