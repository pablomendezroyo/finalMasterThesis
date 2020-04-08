import json
from web3 import Web3
infura_url = "https://goerli.infura.io/v3/21eb6a6c17fc415eb9f4cf08d91f9f93"
web3 = Web3(Web3.HTTPProvider(infura_url))

#abi = JSON that describes SC looks like
abi = json.loads('[{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceReceived","outputs":[{"internalType":"uint256","name":"totalBalance","type":"uint256"},{"internalType":"uint256","name":"numPayments","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sendMoney","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_to","type":"address"}],"name":"withdrawAllMoney","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawMoney","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

# address of the deployed smart contract
address_contract = "0x9DE5F2CAa47CD11a8FD097DD396754474d7f95FB"
address_account_1 = "0x61D38805c04C8cb9b5D71bdAfaD874Fa2ac091D3"
address_account_2 = "0x4B165B929Aa5120e6848a9d0d742faD0929e80b5"
private_key_1 = "817F2FE20B21A70670937550E3F83209DFB3C80E6C0BD6C08DDA3DD7A3F665AF"

contract = web3.eth.contract(address = address_contract, abi = abi)

variable = contract.functions.getBalance().call()
balance_1 = web3.eth.getBalance(address_account_1)
balance_2 = web3.eth.getBalance(address_account_2)

print("The balance of account 1 is: ", web3.fromWei(balance_1, "ether"))
print("The balance of account 2 is: ", web3.fromWei(balance_2, "ether"))
print(variable)

nonce = web3.eth.getTransactionCount(address_account_1)

tx = {
    'nonce': nonce,
    'to': address_account_2,
    'value': web3.toWei(0.01, 'ether'),
    'gas': 30000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key_1)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

'''w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/YOUR_PROJECT_ID"))

contract_ = w3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin'])

acct = w3.eth.account.privateKeyToAccount(privateKey)

construct_txn = contract_.constructor().buildTransaction({
    'from': acct.address,
    'nonce': w3.eth.getTransactionCount(acct.address),
    'gas': 1728712,
    'gasPrice': w3.toWei('21', 'gwei')})

signed = acct.signTransaction(construct_txn)

w3.eth.sendRawTransaction(signed.rawTransaction)'''
