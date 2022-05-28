"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
#import pymysql

class Data:

	def __init__(self):
		self.conn = pymysql.connect(
			host="localhost",
			user="root",
			password="",
			db="cesfam"
			)

		self.cursor = self.conn.cursor()
    #conexion caducar medicamentos
	def InsertItems(self, element):
		#our element contend the name, age and the carreer of the student
		#in position 0, 1, 2
		sql = "insert into medicamentos(id, descripción, fabricante, gramaje, cantidad) values('{}', '{}', '{}', '{}', '{}')".format(element[0],element[1],element[2],element[3],element[4])
		#execute the query
		self.cursor.execute(sql)
		self.conn.commit()#guardamos cambios


	
	def ReturnOneItem(self, ref):
		#we have ref like name of the element
		sql = "select * from medicamento where descripción = '{}'".format(ref)
		self.cursor.execute(sql)
		#return the element or nil
		return self.cursor.fetchone()


	def returnAllElements(self):
		sql = "select * from medicamentos"
		self.cursor.execute(sql)
		return self.cursor.fetchall()


	def Delete(self, ref):
		sql = "delete from medicamentos where descripción = '{}'".format(ref)
		self.cursor.execute(sql)
		self.conn.commit()


	def UpdateItem(self, element, ref):
		#element contains the values and ref is the name of the item that we want change
		sql = "update medicamentos set id = '{}',descripción = '{}', fabricante='{}', gramaje='{}', cantidad='{}'where id = '{}'".format(element[0],element[1],element[2],element[3],element[4], ref)
		#execute the query
		self.cursor.execute(sql)
		self.conn.commit()#guardamos cambios

'''
d = Data()		
users = d.returnAllElements()
for i in users:
	print(i)
'''