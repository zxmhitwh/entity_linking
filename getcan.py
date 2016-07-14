import MySQLdb
from getcanbywiki import *

def getCanByPrior(mention):
	pass

def getCanByMatch(mention):
	canlist = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	mysql = "select entityname from labels  where match(entitystr) against (\""+mention+"\" in natural language mode) limit 5"
	#mysql = "select entityname from labels  where match(entitystr) against (\""+mention+"\" in boolean mode) limit 4"
	cur.execute(mysql)
	resultlist = cur.fetchall()
	for each in resultlist:
		canlist.append(each[0])
	cur.close()
	conn.commit()
	conn.close()
	return canlist


def getCanByLabels(mention):
	canlist = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	stmt = "select entitystr from labels where entityname = \"" + mention + "\""
	cur.execute(stmt)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0])
	cur.close()
	conn.commit()
	conn.close()
	return canlist

def getCanByRedirect(mention):
	canlist = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	stmt = "select redirectname from redirect1 where entityname = \"" + mention + "\""
	cur.execute(stmt)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0])
	cur.close()
	conn.commit()
	conn.close()
	return canlist


def getCanByDisambiguation(mention):
	canlist = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	stmt1 = "select disname  from disambiguation1 where entityname = \"" + mention + "\""
	cur.execute(stmt1)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0])

	stmt2 = "select disname  from disambiguation1 where entityname = \"" + mention + "_(disambiguation)" + "\""
	cur.execute(stmt2)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0])
	return list(set(canlist))

def getCanBy3files(mention):
	canlist = []
	canlist.extend(getCanByLabels(mention))
	canlist.extend(getCanByRedirect(mention))
	canlist.extend(getCanByDisambiguation(mention))
	return list(set(canlist))

def getCanByRule(mention):
	canlist = []
	labelslist = getCanByLabels(mention)
	redirectlist = getCanByRedirect(mention)
	dislist = getCanByDisambiguation(mention)
	canlist.extend(labelslist)
	canlist.extend(redirectlist)
	canlist.extend(dislist)
	if redirectlist != []:
		for can in redirectlist:
			canlist.extend(getCanByLabels(can))
			canlist.extend(getCanByDisambiguation(can))
	if canlist == []:
		canlist = getCanByMatch(mention)
	if canlist == []:
		canlist = get_can(mention,5)
	return list(set(canlist))

def getCanByPrior(mention):
	canlist = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	stmt = "select entity from popularity where mention = \"" + mention + "\""
	cur.execute(stmt)
	result = cur.fetchall()
	if result:
		for each in result:
			canlist.append(each[0])
	cur.close()
	conn.commit()
	conn.close()
	return canlist


def getCanByPrior1(mention,maxnum):
	canlist = []
	conn= MySQLdb.connect(host='localhost',user='root',passwd = '123456',db ='entitylinkdb')
	cur = conn.cursor()
	stmt = "select entity,prob from popularity where mention = \"" + mention + "\""
	cur.execute(stmt)
	result = cur.fetchall()
	if len(result) <= maxnum:
		canlist = [x[0] for x in result]
	else:
		result = sorted(list(result), key=lambda x:float(x[1]),reverse=True)
		canlist = [x[0] for x in result[0:maxnum]]
	for i in canlist:
		if "_(disambiguation)" in i:
			canlist.extend(getCanByDisambiguation(i))
			canlist.remove(i)
	#if result:
	#	for mention,prob in result:
	#		canlist.append([])
	cur.close()
	conn.commit()
	conn.close()
	return canlist

def getCanByPriorRule(mention):
	canlist = []
	#priorlist = getCanByPrior(mention)
	priorlist = getCanByPrior1(mention,10)
	canlist.extend(priorlist)
	if priorlist == []:
		canlist.extend(getCanByRule(mention))
	if canlist == []:
		canlist = getCanByMatch(mention)
	if canlist == []:
		canlist = get_can(mention,5)
	return canlist

def main():
	entitydoc,docmention = get_mention()
	totalnumber = 0
	covernumber = 0
	docnumber = 0
	errorlist = []
	totalcan = 0
	nullnumber = 0
	nulllist = []
	for doc in entitydoc:
		tm = 0
		cn = 0
		docnumber += 1
		print docnumber
		mentionlist = docmention[doc]
		for mention,entityname in mentionlist:
			tm += 1
			totalnumber += 1
			result = getCanByRule(mention)
			if result == []:
				nulllist.append(mention)
				nullnumber += 1
			totalcan += len(result)
			if entityname in result:
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
	print nullnumber
	print nulllist

def main1():
	entitydoc,docmention = get_mention()
	totalnumber = 0
	covernumber = 0
	docnumber = 0
	errorlist = []
	totalcan = 0
	nullnumber = 0
	nulllist = []
	for doc in entitydoc:
		tm = 0
		cn = 0
		docnumber += 1
		print docnumber
		mentionlist = docmention[doc]
		for mention,entityname in mentionlist:
			tm += 1
			totalnumber += 1
			#result = getCanByRedirect(mention)
			#result = getCanByPrior1(mention,10)
			result = getCanByPriorRule(mention)
			if result == []:
				nulllist.append(mention)
				nullnumber += 1
			totalcan += len(result)
			if entityname in result:
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
	print nullnumber
	print nulllist

if __name__ == '__main__':
	main1()
	#print getCanByPrior1("China",10)