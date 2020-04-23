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

def get_latest_block():
    block_number = web3.eth.blockNumber
    return block_number

def listen_to_events(_topic_buyer, _topic_seller, _out_qeue):
    from_block = get_latest_block()
    while(1):
        event_filter = web3.eth.filter({
            "fromBlock": from_block, 
            "toBlock": 'latest', 
            "address": address_contract, 
            # First item is the hash of event name, Second is the buyer, Third is the seller
            "topics": [None, _topic_buyer, _topic_seller]})
        print(event_filter)
        event_list = event_filter.get_all_entries()
        print(event_list)

        if(len(event_list) > 0):
            print("NEW EVENT")
            for k1, v1 in event_list[0].items():
                if(k1 == 'data'):
                    amount_kw = int(v1[:66], 16)
                    total_money = int(v1[67:], 16)
                
                if(k1 == 'topics'):
                    topic_buyer = v1[1].hex()
                    topic_seller = v1[2].hex()
            
            if(_topic_buyer == topic_buyer or _topic_seller == topic_seller):
                print("EVENT FOUND!")
                print("Amount kw: {}, total money: {}".format(amount_kw, total_money))
                _out_qeue.put_nowait(amount_kw)
                _out_qeue.put_nowait(total_money)
                return amount_kw, total_money
                    
        elif(len(event_list) == 0):
            print("NO NEW EVENTS YET")
        time.sleep(10)

def loop():
    _connection = establish_connection()
    write_db(_connection)

def main():
    _connection = establish_connection()
    #write_db(_connection)

    read_db(_connection)

if __name__ == '__main__':
    main()
