import pandas as pd
import pymysql
import pymysql.cursors
#from backend.smartContract_Interaction.Interact_with_real_smart_contr import listen_to_events

def establish_connection():
    connection = pymysql.connect(host='pythondb.cwi83idjai0q.eu-west-3.rds.amazonaws.com',
                                user='admin',
                                password='Telefonista1',
                                port=int(3306),
                                db='prueba',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def read_db(connection):
    try:
        # Create a cursor object
        cursorObject = connection.cursor()                                     

        #sqlQuery = "SHOW TABLE STATUS"  
        sqlQuery = "SELECT * FROM Transactions"  

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
        #sqlQuery = "CREATE TABLE Transactions(Buyer varchar(32), Seller varchar(32), Amount_KW int, Total_value int)"   
        sqlQuery = "INSERT INTO Transactions(Buyer, Seller, Amount_KW, Total_value) VALUES (\"Albert\", \"Einstein\", 10, 5);"

        # Execute the sqlQuery
        cursorObject.execute(sqlQuery)
        # commit changes
        connection.commit()

    except Exception as e:

        print("Exeception occured:{}".format(e))

    finally:

        connection.close()


def main():
    _connection = establish_connection()
    #write_db(_connection)

    read_db(_connection)

if __name__ == '__main__':
    main()



