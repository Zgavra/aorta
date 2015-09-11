__author__ = 'Gavra'

import MySQLdb as mdb
import sys



# CREATE A NEW TABLE and INSERT SOME VALUES
def createTable(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Fudbaleri")
        cur.execute("CREATE TABLE Fudbaleri(Id INT PRIMARY KEY AUTO_INCREMENT, \
                     Name VARCHAR(100))")
        cur.execute("INSERT INTO Fudbaleri(Name) VALUES('Steven Gerrard')")
        cur.execute("INSERT INTO Fudbaleri(Name) VALUES('Emre Can')")
        cur.execute("INSERT INTO Fudbaleri(Name) VALUES('Martin Skrtel')")
        cur.execute("INSERT INTO Fudbaleri(Name) VALUES('Philippe Coutinho')")
        cur.execute("INSERT INTO Fudbaleri(Name) VALUES('Roberto Firmino')")



# RETRIEVE
def retrieveTable(con):
    with con:

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM Fudbaleri")

        rows = cur.fetchall()

        for row in rows:
            print row["Id"], row["Name"]



# UPDATE
def updateRow(con):
    with con:

        cur = con.cursor()

        cur.execute("UPDATE Fudbaleri SET Name = %s WHERE Id = %s",
            ("nesto nesto", "4"))

        print "Number of rows updated:",  cur.rowcount



# DELETE
def deleteRow(con):
    with con:

        cur = con.cursor()

        cur.execute("DELETE FROM Fudbaleri WHERE Id = %s", "2")

        print "Number of rows deleted:", cur.rowcount



try:
    con = mdb.connect('localhost:8080', 'root', 'toor', 'Fudbaleri');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()

    print "Database version : %s " % ver


    # CRUD OPERATIONS
    createTable(con)
    retrieveTable(con)
    updateRow(con)
    deleteRow(con)



except mdb.Error, e:

    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)


finally:

    if con:
        con.close()