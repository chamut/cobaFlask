import mysql.connector


class Cobalagi():

    def getdata(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pedigree_db"
        )
        print(mydb)
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT stat, lastname FROM family")
        myresult = mycursor.fetchall()
        return myresult
