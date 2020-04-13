import json
from web3 import Web3
infura_url = "https://goerli.infura.io/v3/21eb6a6c17fc415eb9f4cf08d91f9f93"
web3 = Web3(Web3.HTTPProvider(infura_url))

# CONTRACT
abi = json.loads('[	{		"inputs": [			{				"internalType": "address payable",				"name": "_seller",				"type": "address"			},			{				"internalType": "uint256",				"name": "_amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_price_min_kwh",				"type": "uint256"			}		],		"name": "matchBuyer",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"anonymous": false,		"inputs": [			{				"indexed": false,				"internalType": "bool",				"name": "_status",				"type": "bool"			}		],		"name": "matchFound",		"type": "event"	},	{		"inputs": [			{				"internalType": "address",				"name": "_buyer",				"type": "address"			},			{				"internalType": "uint256",				"name": "_amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_price_max_kwh",				"type": "uint256"			}		],		"name": "matchSeller",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"inputs": [],		"name": "sendMoney",		"outputs": [],		"stateMutability": "payable",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "_amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_price_max_kwh",				"type": "uint256"			}		],		"name": "setBuyer",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "_amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "_price_min_kwh",				"type": "uint256"			}		],		"name": "setSeller",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "balanceReceived",		"outputs": [			{				"internalType": "uint256",				"name": "totalBalance",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "numPayments",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "buyer",		"outputs": [			{				"internalType": "address",				"name": "addressBuyer",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_max_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [],		"name": "getBalance",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"name": "Offers_Buyer_Array",		"outputs": [			{				"internalType": "address",				"name": "addressBuyer",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_max_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"name": "Offers_Seller_Array",		"outputs": [			{				"internalType": "address payable",				"name": "addressSeller",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_min_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "",				"type": "address"			}		],		"name": "seller",		"outputs": [			{				"internalType": "address payable",				"name": "addressSeller",				"type": "address"			},			{				"internalType": "uint256",				"name": "amount_min_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "amount_max_kw",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "price_min_kwh",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	}]')
address_contract = "0xdBc26FfeFd95b0F864C401F9216A30344c1b2e65"

# ACCOUNTS
address_account_1 = "0x61D38805c04C8cb9b5D71bdAfaD874Fa2ac091D3"
address_account_2 = "0x4B165B929Aa5120e6848a9d0d742faD0929e80b5"
private_key_1 = "817F2FE20B21A70670937550E3F83209DFB3C80E6C0BD6C08DDA3DD7A3F665AF"
private_key_2 = "530C781BF8682172AA10C2A81CF9D9AE5E97CF99254550DAE0BB4DBECD6ED147"

contract = web3.eth.contract(address = address_contract, abi = abi)

# SET SELLER
def set_Seller():
    nonce1 = web3.eth.getTransactionCount(address_account_1)

    transaction_setSeller = contract.functions.setSeller(
        1, 3, 2).buildTransaction({
            'gas': 1000000,
            'gasPrice': web3.toWei('1', 'gwei'),
            'from': address_account_1,
            'nonce': nonce1
        })
    print(transaction_setSeller)
    signed_txn = web3.eth.account.signTransaction(transaction_setSeller, private_key=private_key_1)
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(signed_txn)

# SET MONEY
def set_Money():
    nonce2 = web3.eth.getTransactionCount(address_account_2)

    transaction_sendMoney = contract.functions.sendMoney().buildTransaction({
            'gas': 1000000,
            'gasPrice': web3.toWei('1', 'gwei'),
            'value': web3.toWei(0.1, 'ether'),
            'from': address_account_2,
            'nonce': nonce2
        })
    print(transaction_sendMoney)
    signed_txn = web3.eth.account.signTransaction(transaction_sendMoney, private_key=private_key_2)
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(signed_txn)


# SET BUYER
def set_Buyer():
    nonce2 = web3.eth.getTransactionCount(address_account_2)

    transaction_setBuyer = contract.functions.setBuyer(
        2, 3).buildTransaction({
            'gas': 1000000,
            'gasPrice': web3.toWei('1', 'gwei'),
            'from': address_account_2,
            'nonce': nonce2
        })
    print(transaction_setBuyer)
    signed_txn = web3.eth.account.signTransaction(transaction_setBuyer, private_key=private_key_2)
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(signed_txn)

# PRINT BALANCES
def get_balance():
    variable = contract.functions.getBalance().call()
    balance_1 = web3.eth.getBalance(address_account_1)
    balance_2 = web3.eth.getBalance(address_account_2)

    print("The balance of account 1 is: ", web3.fromWei(balance_1, "ether"))
    print("The balance of account 2 is: ", web3.fromWei(balance_2, "ether"))
    print(variable)

