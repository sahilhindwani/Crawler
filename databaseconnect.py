import MySQLdb

class Database:
	def __init__(self,tname,dbname):
		self.table_name=tname
		self.db_name=dbname

	def connect(self):
			self.db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db=str(self.db_name),unix_socket="opt/lampp/var/mysql/mysql.sock")
	def insert(self,values):
		sql="Insert into "+str(self.table_name)+" (links,keyword) values ('"+str(values[1])+"','"+str(values[2])+"');"
#	print sql
		cursor=self.db.cursor();
		try:
			cursor.execute(sql)
			self.db.commit()
		except:
			print "error"
			self.db.rollback()

	def insert1(self,values):
                sql="Insert into "+str(self.table_name)+" (username,link_name) values ('"+str(values[0])+"','"+str(values[1])+"');"
		cursor=self.db.cursor();
		try:
			cursor.execute(sql)
	                self.db.commit()
	      	except:
			print ""
			self.db.rollback()
	
	def view(self,query):
		sql="select * from "+str(self.table_name)+" where username='"+str(query[0])+"'and link_name='"+str(query[1])+"';"
#print sql
		try:
			cursor=self.db.cursor()
			cursor.execute(sql)
			results=cursor.fetchall()
#			print results[1]
			for row in results:
				u=row[1]
			return  u
		except:
			return "error"

	def close(self):
		self.db.close()
