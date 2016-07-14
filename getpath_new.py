#coding=utf8
import MySQLdb
import networkx as nx
import time

def getEntityPair(entitydic): #得到候选实体对
	entitypairarray = []
	for entity1 in entitydic.keys():
		for entity2 in entitydic.keys():
			if entity1 != entity2:
				for each1 in entitydic[entity1]:
					for each2 in entitydic[entity2]:
						entitypairarray.append([each1,each2])
	entitypairarraynew = []
	for entitypair in entitypairarray:
		entity1,entity2 = entitypair
		if [entity2,entity1] not in entitypairarraynew:
			entitypairarraynew.append(entitypair)
	return entitypairarraynew

#只适合路径为2的一个路径搜索方法
def getPairPath(entitypair):
	patharray = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb',port=3306)
	cur1 = conn.cursor()
	cur2 = conn.cursor()
	cur3 = conn.cursor()
	cur4 = conn.cursor()
	mysql1 = "select entityname,linkname from pagelinks where entityname = \""+entitypair[0]+"\" and linkname = \""+entitypair[1]+"\""
	mysql2 = "select entityname,linkname from pagelinks where entityname = \""+entitypair[1]+"\" and linkname = \""+entitypair[0]+"\""
	mysql3 = "select entityname,linkname from pagelinks where entityname = \""+entitypair[0]+"\""
	mysql4 = "select entityname,linkname from pagelinks where entityname = \""+entitypair[1]+"\""
	cur1.execute(mysql1)
	resultlist = cur1.fetchall()
	for eachresult in resultlist:
		print eachresult
		patharray.append(eachresult)
	cur2.execute(mysql2)
	resultlist = cur2.fetchall()
	for eachresult in resultlist:
		print eachresult
		patharray.append(eachresult)
	linkset1 = []
	linkset2 = []
	cur3.execute(mysql3)
	resultlist = cur3.fetchall()
	for eachresult in resultlist:
		linkset1.append(eachresult)
	cur4.execute(mysql4)
	resultlist = cur4.fetchall()
	for eachresult in resultlist:
		linkset2.append(eachresult)
	for entityname1,linkname1 in linkset1:
		for entityname2,linkname2 in linkset2:
			if linkname1 == linkname2:
				print entityname1,linkname1
				print entityname2,linkname2
				patharray.append((entityname1,linkname1))
				patharray.append((entityname2,linkname2))
	return patharray

def getAllpath(entitypairarray):
	allpath = []
	for entitypair in entitypairarray:
		patharray = getPairPath(entitypair)
		allpath.extend(patharray)
	allpath = set(allpath)
	return allpath

'''
def getPairPath(entitypair,len):
	patharray = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb',port=3306)
	cur = conn.cursor()
	mysql = getSQL(entitypair,len)
	cur.execute(mysql)
	resultlist = cur.fetchall()
	for eachresult in resultlist:
		print eachresult
		patharray.append(eachresult)

def getAllpath(entitypairarray,len):
	allpath = []
	for entitypair in entitypairarray:
		for eachlength in range(len):
			patharray = getPairPath(entitypair,(eachlength+1))
			allpath.extend(patharray)
	allpath = set(allpath)
	return allpath
'''

if __name__ == '__main__':
	start = time.clock()
	candidates = {}
	candidates['Romney'] = ['Romney_Marsh', 'New_Romney', 'Mitt_Romney', 'Baron_Romney']
	candidates['Santorum'] = ['Karen_Santorum', 'Rick_Santorum', 'Santorum_slang', 'Rick_santorum']
	candidates['Huckabee'] = ['Mike_Huckabee', 'Mike+huckabee', 'David_Huckabee', 'Janet_Huckabee']
	candidates['Gingrich'] = ['Newt_Gingrich', 'NewtGingrich', 'John_Gingrich', 'Felix_Gingrich']
	print candidates.items()[0]
	print candidates.items()[1]
	print candidates.items()[2]
	print candidates.items()[3]
	
	entitypairarray = getEntityPair(candidates)
	print len(entitypairarray)
	patharray = getAllpath(entitypairarray)
	resultfile = open('pathfile1.txt','w')
	for eachpath in patharray:
		string = ''
		for i in eachpath:
			string = string + i + ' '
		string = string + '\n'
		resultfile.write(string)
	end = time.clock()
	print end-start,'seconds process time'
