import pandas as pd
import pymysql
import pymysql.cursors

def establish_connection():
    connection = pymysql.connect(host='pythondb.cwi83idjai0q.eu-west-3.rds.amazonaws.com',
                                user='admin',
                                password='Telefonista1',
                                port=int(3306),
                                db='prueba',
                                cursorclass=pymysql.cursors.DictCursor)

    print(connection)

def read_db(connection):

    try:
        # Create a cursor object
        cursorObject = connection.cursor()                                     

        #sqlQuery = "SHOW TABLE STATUS"  
        sqlQuery = "SHOW COLUMNS FROM Transactions"  

        # Execute the sqlQuery
        cursorObject.execute(sqlQuery)

        #Fetch all the rows
        rows = cursorObject.fetchall()

        for row in rows:

            print(row)

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        connection.close()

def write_db(connection):
    try:
        # Create a cursor object
        cursorObject = connection.cursor()                                     

        # SQL query string
        sqlQuery = "CREATE TABLE Transactions(Buyer varchar(32), Seller varchar(32), Amount_KW int, Total_value int)"   

        # Execute the sqlQuery
        cursorObject.execute(sqlQuery)

    except Exception as e:

        print("Exeception occured:{}".format(e))

    finally:

        connection.close()




