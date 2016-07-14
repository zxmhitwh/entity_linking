import MySQLdb
from getcanbywiki import *

def getcandidate(mention):
	canlist = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	stmt1 = "select entitystr from labels where entityname = \"" + mention + "\""
	cur.execute(stmt1)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0].lower())

	stmt5 = "select entityname from pagelinks where entityname = \"" + mention + "\""
	cur.execute(stmt5)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0].lower())

	stmt6 = "select linkname from pagelinks where entityname = \"" + mention + "\""
	cur.execute(stmt6)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0].lower())	

	stmt2 = "select redirectname from redirect where entityname = \"" + mention + "\""
	cur.execute(stmt2)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0].lower())


	stmt3 = "select disname  from disambiguation where entityname = \"" + mention + "\""
	cur.execute(stmt3)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0].lower())

	stmt4 = "select disname  from disambiguation where entityname = \"" + mention + "_(disambiguation)" + "\""
	cur.execute(stmt4)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0].lower())

	#print len(canlist)

	canlist = set(canlist)
	dellist = []
	for can in canlist:
		if "_(disambiguation)" in can:
			dellist.append(can)
			stmt = "select disname  from disambiguation where entityname = \"" + can + "_(disambiguation)" + "\""
			cur.execute(stmt)
			result = cur.fetchall()
			if result:
				for each in result:
					if each[0].lower() not in canlist:
						canlist.append(each[0].lower())
	canlist = list(canlist - set(dellist))
	return canlist		
	print canlist

def can_test():
	entitydoc,docmention = get_mention()
	totalnumber = 0
	covernumber = 0
	docnumber = 0
	errorlist = []
	totalcan = 0
	for doc in entitydoc:
		tm = 0
		cn = 0
		docnumber += 1
		print docnumber
		mentionlist = docmention[doc]
		for mention,entityname in mentionlist:
			tm += 1
			totalnumber += 1
			result = getcandidate(mention)
			totalcan += len(result)
			if entityname.lower() in result:
				cn += 1
				covernumber += 1
			else:
				errorlist.append([mention,entityname])
		print "**********************"
		print "total:" + str(tm)
		print "cover:" + str(cn)
	print totalnumber
	print covernumber
	print float(covernumber)/totalnumber
	print float(totalcan)/totalnumber
	#print errorlist

if __name__ == '__main__':
	#can_test()
	#print len(getcandidate("China"))