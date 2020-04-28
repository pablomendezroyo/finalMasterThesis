**TERRAFORM AMAZON WEB SERVICES IMPLEMENTATION**
_This folder contains the code needed to implement the infraestructure described in previous sections, an ec2 instance and the relational database, includding the corresponding network infraestructure._

**Steps for infraestructure deployment**
1. First step: download the resources described in the main.tf file by tipping the command: _terraform init_
2. Second step: visualize the implementation by tipping the command: _terraform plan_
3. Third step: apply the changes in the cloud by tipping the command: _terraform apply_

**Steps for loging into the instance ec2**
1. Create ssh keys in pem format using amazon platform and assign them to the instance created.
2. Type the following command in a terminal using te path of the ssh keys and the host of the ec2 created:
    _ssh -i <ssh pem keys path> <ec2 hostname>_

**Steps for connectig to the rds inside the ec2 instance**
1. Install the following library: _sudo install mysql-core-5.7_
2. Type the following command inside the ec2: _mysql -h <rds hostname> -p <port opened> -u <username> -p <password>_

**Steps for copying a file into the ec2, in thi project will be a python script**
1. Type the following command in a terminal: _scp -i <ssh key pem path> <python script path> <ec2 hostname/python script>_