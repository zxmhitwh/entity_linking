import wikipedia
import MySQLdb
import threading

def get_can(mention,maxnum):
	resultlist = wikipedia.search(mention,results=maxnum)
	returnlist = []
	for each in resultlist:
		returnlist.append("_".join(each.encode("utf-8").split()))
	return returnlist

def get_mention():
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	stmt1 = "select distinct docid from tac_kbp_2014"
	cur.execute(stmt1)
	docs = cur.fetchall()
	entitydoc = []
	for doc in docs:
		entitydoc.append(doc[0])

	docmention = {}
	for doc in entitydoc:
		sql = "select mention,entityname from tac_kbp_2014 where docid = \"" + doc + "\""
		cur.execute(sql)
		result = cur.fetchall()
		mentionlist = []
		for mention,entityname in result:
			mentionlist.append([mention,entityname])
		docmention[doc] = mentionlist
	return entitydoc,docmention

def test(entitydoc,docmention):
	totalnumber = 0
	covernumber = 0
	docnumber = 0
	for doc in entitydoc:
		tm = 0
		cn = 0
		docnumber += 1
		print docnumber
		mentionlist = docmention[doc]
		for mention,entityname in mentionlist:
			tm += 1
			totalnumber += 1
			result = get_can(mention,5)
			if entityname in result:
				cn += 1
				covernumber += 1
		print "**********************"
		print "total:" + str(tm)
		print "cover:" + str(cn)
	print totalnumber
	print covernumber

class getentity(threading.Thread):
	def __init__(self,mention,maxnum):
		threading.Thread.__init__(self)
		self.mention = mention
		self.maxnum = maxnum
		self.resultlist = []

	def run(self):
		self.resultlist = get_can(self.mention,self.maxnum)

def test1(entitydoc,docmention,maxnum):
	totalnumber = 0
	covernumber = 0
	docnumber = 0
	for doc in entitydoc:
		docnumber += 1
		mentionlist = docmention[doc]
		threads = []
		entitylist = []
		resultlist = []
		for mention,entityname in mentionlist:
			threads.append(getentity(mention,maxnum))
			entitylist.append(entityname)
	 	for t in threads:
	 		t.start()
	 	for t in threads:
	 		t.join()
	 		resultlist.append(t.resultlist)
	 	tm = 0
	 	cn = 0
	 	for i in range(len(entitylist)):
	 		tm += 1
	 		totalnumber += 1
	 		if entitylist[i] in resultlist[i]:
	 			cn += 1
	 			covernumber += 1
	 	print "***************doc:" + str(docnumber) + "*************"
		print "total:" + str(tm)
		print "cover:" + str(cn)
	print totalnumber
	print covernumber
	print float(covernumber)/totalnumber	

		

if __name__ == '__main__':
	entitydoc,docmention = get_mention()
	test1(entitydoc,docmention,10)
	#print get_can("PRC",15)