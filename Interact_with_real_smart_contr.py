import json
from web3 import Web3
infura_url = "https://goerli.infura.io/v3/21eb6a6c17fc415eb9f4cf08d91f9f93"
web3 = Web3(Web3.HTTPProvider(infura_url))

#abi = JSON that describes SC looks like
abi = json.loads('[{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceReceived","outputs":[{"internalType":"uint256","name":"totalBalance","type":"uint256"},{"internalType":"uint256","name":"numPayments","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sendMoney","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_to","type":"address"}],"name":"withdrawAllMoney","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawMoney","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

# address of the deployed smart contract
address_contract = "0x9DE5F2CAa47CD11a8FD097DD396754474d7f95FB"

contract = web3.eth.contract(address = address_contract, abi = abi)

variable = contract.functions.getBalance().call()
balance = web3.eth.getBalance("0x4B165B929Aa5120e6848a9d0d742faD0929e80b5")

print(web3.fromWei(balance, "ether"))
print(variable)
