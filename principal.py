# pip install PyMySQL
import pymysql

#Conexion a traves de clasess

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', #ip
            user='root',
            password='@MAsr1234@',
            db='CLIENTES'    
        )
        
        self.cursor = self.connection.cursor()
        print("Conexi[on exitosa!")
        print("\n")

    def select_person(self,id):
        sql = 'SELECT id, nombre, apellido, direccion, email FROM CLIENTES WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            #fetchone porque es 1 solo resultado.
            person = self.cursor.fetchone()

            #Printeo datos extraidos de la base de datos
            print("Id:",person[0])
            print("nombre:",person[1])
            print("apellido:",person[2])
            print("direccion:",person[3])
            print("email:",person[4])
            
        except Exception as e:
            raise
            #Aun no se ha creado codigo para majear las excep..


    def select_all_person(self):
        sql = 'SELECT * FROM CLIENTES'

        try:
            self.cursor.execute(sql)
            #fetchall porque son varios resultados o todos
            persons = self.cursor.fetchall()

            for person in persons:
                #Printeo datos extraidos de la base de datos
                print("Id:",person[0])
                print("nombre:",person[1])
                print("apellido:",person[2])
                print("direccion:",person[3])
                print("email:",person[4])
                print("\n")
            
        except Exception as e:
            raise
            #AUn no se ha creado codigo para majear las excep..
    
    def update_person(self,id,nombre):
        
        #sentencia sql
        sql =  "UPDATE CLIENTES SET nombre='{}' WHERE id={}".format(nombre,id)

        try:
            self.cursor.execute(sql)
            self.connection.commit() #Guarda Cambios
            #Persistencia del update, inset o delete
        except Exception as e:
            raise
    
    def add_person(self,nombre,apellido,direccion,email):
        #sentencia SQL - lenguaje de consultas
        sql = "INSERT INTO CLIENTES (nombre,apellido,direccion,email) VALUES('{}','{}','{}','{}')".format(nombre,apellido,direccion,email)

        try:
            self.cursor.execute(sql)
            self.connection.commit() #Persistencia
        except Exception as e:
            raise
    
    def delete_person(self,id):
        #sentencia sql
        sql = "DELETE FROM CLIENTES WHERE id='{}'".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit() # Pesistencia
        except Exception as e:
            raise


    def close(self):
        self.connection.close()



# creo un objeto DataBase
database = DataBase()
# llamo al metodo select person del objeto de la clase DataBase
#database.select_person(5)
#database.update_person(5,'JAIROTE')
#database.select_all_person()
#database.select_person(5)
#database.add_person('Florelbita','Ramirez','Calle 117a','florelba-rc@hotmail.com')
#database.delete_person(7)
#database.delete_person(8)
database.select_all_person()


database.close()