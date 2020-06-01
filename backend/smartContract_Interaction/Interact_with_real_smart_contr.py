import json
import time
from web3 import Web3
from config import address_account_1, address_account_2, private_key_1, private_key_2, topic_account_1, topic_account_2, address_contract

#infura_url = "https://goerli.infura.io/v3/21eb6a6c17fc415eb9f4cf08d91f9f93"
websocket = "wss://goerli.infura.io/ws/v3/21eb6a6c17fc415eb9f4cf08d91f9f93"
#local_url = "HTTP://127.0.0.1:7545"

#web3 = Web3(Web3.HTTPProvider(infura_url))
web3 = Web3(Web3.WebsocketProvider(websocket))
#web3 = Web3(Web3.HTTPProvider(local_url))

abi = json.loads('[	{		"anonymous": false,		"inputs": [			{				"indexed": false,				"internalType": "bool",				"name": "_status",				"type": "bool"			}		],		"name": "matchFound",		"type": "event"	},	{		"inputs": [],		"name": "sendMoney",		"outputs": [],		"stateMutability": "payable",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "_amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_price_max_kwh",				"type": "uint256"			}		],		"name": "setBuyer",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "_amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_price_min_kwh",				"type": "uint256"			}		],		"name": "setSeller",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"anonymous": false,		"inputs": [			{				"indexed": true,				"internalType": "address",				"name": "_buyer",				"type": "address"			},			{				"indexed": true,				"internalType": "address",				"name": "_seller",				"type": "address"			},			{				"indexed": false,				"internalType": "uint256",				"name": "_amount_kw",				"type": "uint256"			},			{				"indexed": false,				"internalType": "uint256",				"name": "_price",				"type": "uint256"			}		],		"name": "transactionDone",		"type": "event"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "balanceReceived",		"outputs": [			{				"internalType": "uint256",				"name": "totalBalance",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "numPayments",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "buyer",		"outputs": [			{				"internalType": "address",				"name": "addressBuyer",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_max_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "_amountInWei",				"type": "uint256"			}		],		"name": "convertWeiToEther",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "pure",		"type": "function"	},	{		"inputs": [],		"name": "getBalance",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"name": "Offers_Buyer_Array",		"outputs": [			{				"internalType": "address",				"name": "addressBuyer",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_max_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"name": "Offers_Seller_Array",		"outputs": [			{				"internalType": "address payable",				"name": "addressSeller",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_min_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "seller",		"outputs": [			{				"internalType": "address payable",				"name": "addressSeller",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_min_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	}]')

contract = web3.eth.contract(address = address_contract, abi = abi)

# SET SELLER
def set_Seller(_address_account, _private_key, _amount_min_kw, _amount_max_kw, _price_min_kwh):
    nonce1 = web3.eth.getTransactionCount(_address_account)

    construct_txn = contract.functions.setSeller(
        int(_amount_min_kw), int(_amount_max_kw), int(_price_min_kwh)).buildTransaction({
            'gas': 1000000,
            'gasPrice': web3.toWei('1', 'gwei'),
            'from': _address_account,
            'nonce': nonce1
        })
    
    signed_txn = web3.eth.account.signTransaction(construct_txn, private_key=_private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    #print(construct_txn)
    #print(signed_txn)
    #print(tx_receipt)

    return tx_receipt

# SET MONEY
def set_Money(_address_account, _private_key, amount):
    nonce = web3.eth.getTransactionCount(_address_account)

    construct_txn = contract.functions.sendMoney().buildTransaction({
            'gas': 1000000,
            'gasPrice': web3.toWei('1', 'gwei'),
            'value': web3.toWei(amount, 'wei'),
            'from': _address_account,
            'nonce': nonce
        })
    
    signed_txn = web3.eth.account.signTransaction(construct_txn, private_key=_private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    #print(construct_txn)
    #print(signed_txn)
    #print(tx_receipt)

    return tx_receipt


# SET BUYER
def set_Buyer(_address_account, _private_key, _amount_kw, _price_max_kwh):
    nonce = web3.eth.getTransactionCount(_address_account)

    construct_txn = contract.functions.setBuyer(
        int(_amount_kw), int(_price_max_kwh)).buildTransaction({
            'gas': 1000000,
            'gasPrice': web3.toWei('1', 'gwei'),
            'from': _address_account,
            'nonce': nonce
        })
    
    signed_txn = web3.eth.account.signTransaction(construct_txn, private_key=_private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    
    #print(construct_txn)
    #print(signed_txn)
    #print(tx_receipt)

    return tx_receipt

## BALANCES ##

# Contract balance
def get_balance_contract():
    balance_contract = contract.functions.getBalance().call()
    return balance_contract

# Account total balance
def get_balance_account(_address_account):
    balance = web3.eth.getBalance(_address_account)
    balance_ether = web3.fromWei(balance, "ether")
    return balance_ether

# Account balance in contract and num payments
def get_balance_received(_address_account):
    balance_received_list = contract.functions.balanceReceived(_address_account).call()
    balance_received_wei = balance_received_list[0]
    balance_received_ether = web3.fromWei(balance_received_wei, "ether")
    num_payments = balance_received_list[1]
    return balance_received_wei


## EVENTS ##
def listen_to_events(_topic_buyer, _topic_seller, _out_qeue):
    from_block = get_latest_block()
    #from_block = 2536028
    while(1):
        event_filter = web3.eth.filter({
            "fromBlock": from_block, 
            "toBlock": 'latest', 
            "address": address_contract, 
            # First item is the hash of event name, Second is the buyer, Third is the seller
            "topics": [None, _topic_buyer, _topic_seller]})
        #print(event_filter)
        event_list = event_filter.get_all_entries()
        #print(event_list)

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

def get_latest_block():
    block_number = web3.eth.blockNumber
    return block_number


## MAIN ##
def main(): 
    pass
    

if __name__ == '__main__':
    main()