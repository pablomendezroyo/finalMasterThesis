import pandas as pd
import pymysql
import pymysql.cursors
import json
import time
from web3 import Web3

websocket = "wss://goerli.infura.io/ws/v3/21eb6a6c17fc415eb9f4cf08d91f9f93"
web3 = Web3(Web3.WebsocketProvider(websocket))

address_contract = "0xD7a1e535275F9C28161b4aB8D6A2e437d1008e93"
abi = json.loads('[	{		"anonymous": false,		"inputs": [			{				"indexed": false,				"internalType": "bool",				"name": "_status",				"type": "bool"			}		],		"name": "matchFound",		"type": "event"	},	{		"inputs": [],		"name": "sendMoney",		"outputs": [],		"stateMutability": "payable",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "_amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_price_max_kwh",				"type": "uint256"			}		],		"name": "setBuyer",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "_amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_price_min_kwh",				"type": "uint256"			}		],		"name": "setSeller",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"anonymous": false,		"inputs": [			{				"indexed": true,				"internalType": "address",				"name": "_buyer",				"type": "address"			},			{				"indexed": true,				"internalType": "address",				"name": "_seller",				"type": "address"			},			{				"indexed": false,				"internalType": "uint256",				"name": "_amount_kw",				"type": "uint256"			},			{				"indexed": false,				"internalType": "uint256",				"name": "_price",				"type": "uint256"			}		],		"name": "transactionDone",		"type": "event"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "balanceReceived",		"outputs": [			{				"internalType": "uint256",				"name": "totalBalance",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "numPayments",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "buyer",		"outputs": [			{				"internalType": "address",				"name": "addressBuyer",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_max_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "_amountInWei",				"type": "uint256"			}		],		"name": "convertWeiToEther",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "pure",		"type": "function"	},	{		"inputs": [],		"name": "getBalance",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"name": "Offers_Buyer_Array",		"outputs": [			{				"internalType": "address",				"name": "addressBuyer",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_max_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"name": "Offers_Seller_Array",		"outputs": [			{				"internalType": "address payable",				"name": "addressSeller",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_min_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "seller",		"outputs": [			{				"internalType": "address payable",				"name": "addressSeller",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_min_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	}]')
contract = web3.eth.contract(address = address_contract, abi = abi)



def establish_connection():
    connection = pymysql.connect(host='pythondb.cwi83idjai0q.eu-west-3.rds.amazonaws.com',
                                user='admin',
                                password='Telefonista1',
                                port=int(3306),
                                db='prueba',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def close_connection(_connection):
    _connection.close()

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

def write_db(connection, _buyer, _seller, _amountkw, _total_value):
    try:
        # Create a cursor object
        cursorObject = connection.cursor()                                     

        # SQL query string
        #sqlQuery = "CREATE TABLE Transactions(Buyer varchar(32), Seller varchar(32), Amount_KW int, Total_value int)"   
        sqlQuery = "INSERT INTO Transactions(Buyer, Seller, Amount_KW, Total_value) VALUES (\"{}\", \"{}\", {}, {});".format(_buyer, _seller, _amountkw, _total_value)

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

def listen_to_events():
    while(1):
        from_block = get_latest_block()
        event_filter = web3.eth.filter({
            "fromBlock": from_block, 
            "toBlock": 'latest', 
            "address": address_contract, })
            # First item is the hash of event name, Second is the buyer, Third is the seller 0x00000000000000000000000061d38805c04c8cb9b5d71bdafad874fa2ac091d3
            #"topics": [None, _topic_buyer, _topic_seller]})
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
                    buyer = topic_buyer[]
                    topic_seller = v1[2].hex()
            print("Buyer: {}, Seller: {}".format(topic_buyer, topic_seller))
            print("Amount kw: {}, total money: {}".format(amount_kw, total_money))
                    
        elif(len(event_list) == 0):
            print("NO NEW EVENTS YET")
        time.sleep(3)


def main():
    #_connection = establish_connection()
    #write_db(_connection)
    #read_db(_connection)
    listen_to_events()

if __name__ == '__main__':
    main()
