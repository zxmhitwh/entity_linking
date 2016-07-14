#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(host='localhost',user='root',db ='entity')
cur = conn.cursor()
#删除已经存在的数据表
cur.execute("drop table if exists links")
#创建数据表
cur.execute("create table links(id int(10) auto_increment primary key, entityname varchar(100),linkname varchar(100))")
#file = open("testdata.txt")
file = open("E:\page-links_en.nt\page-links_en.nt")
line = file.readline()
while line:
    if '#' in line:
    	pass
    else:
    	a,b = line.strip('<http://dbpedia.org/resource/').strip('> .\n').split('> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/')
    	a = a.replace("'", "''")
    	b = b.replace("'", "''")
    	cur.execute("insert into links(entityname,linkname) values('\""+a+"\"','\""+b+"\"')")
    	print a,b
    line = file.readline()


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()