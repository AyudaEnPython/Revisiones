"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
#import pymysql

class Data:

	def __init__(self):
		self.conn = pymysql.connect(
			host="localhost",
			user="root",
			password="",
			db="prueba"
			)

		self.cursor = self.conn.cursor()



	def InsertItems(self, element):
		#our element contend the name, age and the carreer of the student
		#in position 0, 1, 2
		sql = "insert into persona(Nombre, rut, fecha, descripcion) values('{}', '{}', '{}', '{}')".format(element[0],element[1],element[2],element[3])
		#execute the query
		self.cursor.execute(sql)
		self.conn.commit()#guardamos cambios


	
	def ReturnOneItem(self, ref):
		#we have ref like name of the element
		sql = "select * from persona where Nombre = '{}'".format(ref)
		self.cursor.execute(sql)
		#return the element or nil
		return self.cursor.fetchone()


	def returnAllElements(self):
		sql = "select * from persona"
		self.cursor.execute(sql)
		return self.cursor.fetchall()


	def Delete(self, ref):
		sql = "delete from persona where Nombre = '{}'".format(ref)
		self.cursor.execute(sql)
		self.conn.commit()


	def UpdateItem(self, element, ref):
		#element contains the values and ref is the name of the item that we want change
		sql = "update persona set Nombre = '{}',rut = '{}', fecha='{}', descripcion='{}'where Nombre = '{}'".format(element[0],element[1],element[2],element[3], ref)
		#execute the query
		self.cursor.execute(sql)
		self.conn.commit()#guardamos cambios


'''
d = Data()		
users = d.returnAllElements()
for i in users:
	print(i)
'''