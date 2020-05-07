**FINAL MASTER THESIS**

This project has been entirely developed by Pablo Mendez Royo. The main subjects this project covers are:

**1 Smart contract**
_Develope a smart contract in solidity programming language. The main functionalities for this smart contract is to implement a P2P (peer to peer) energy transaction without intermediaries._

**2 API call REE**
_Furthermore, there have been programmed a code in python to get the values of the energy in the electric market of Spain. These values are taken in real time and the objective is to use them to generate offers/demands in the smart contract based on this value._

**3 Smart contract communication**
_To be able to communicate with the smart contract and use its functions, this projects used web3 for python. Using this libraries, there have been developed 2 classes, seller and buyer. The code will create an instance of the seller class if the battery level is too high, or an instance of the buyer class if the battery level is too low. This algorithm is easy to change in the code. For both cases, seller and buyer, there will be an API call to get the market value and generate an offer/demand by calling functions of the smart contract._

**4 Iac (infraestructure as code) for AWS to implement virtual machine and database using terraform.**
_To improve this project, there have been developed a terraform code to implement an infraestructure in AWS (amazon web services). This infraestructure is composed by a virtual private cloud (VPC), subnet, internet gateway, route table, amazon instance (EC2), and amazon relational database MySQL (RDS). The idea is that the virtual machine EC2 will write every single transaction that is done in the smart contract. Furthermore, at launch time the EC2 is setup with somre python libraries needed for listening the events in the blockchain network where the smart contract have been deployed._

**Configuration**

1. Rquirements: 

To install the requirements is needed pip3 and an actual version of python3.
To install the python libraries type: _pip3 install -r requirements.txt_

2. PYTHONPATH:

In order to be able to use the python modules from this project, it is necessary to let know the python environment of the host machine where is the path for this module.

To do that go to the folder where is located backend and type the following command:
_export PYTHONPATH="PWD"_

This will set the environment variable "PYTHONPATH" with the path of the backend folder, where are located all the modules needed.
