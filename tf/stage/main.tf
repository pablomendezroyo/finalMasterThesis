provider "aws" {
  region = "eu-west-1"
}

## VPC
resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  enable_dns_hostnames = true
}

## Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
}

## Route Table1 associated to gateway
resource "aws_route_table" "igw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route" "r1"{
  route_table_id = aws_route_table.igw.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.gw.id
}

## Route table association r1 (gateway to ec2)
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.ec2-mysql-Subnet.id
  route_table_id = aws_route_table.igw.id
}

## Route table association r2 (gateway to rds)
resource "aws_route_table_association" "b" {
  subnet_id      = aws_subnet.rdsSubnettwo.id
  route_table_id = aws_route_table.igw.id
}

## Subnet rds2
resource "aws_subnet" "rdsSubnettwo" {
  availability_zone = "eu-west-1b"
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
}

## Final subnet rds
resource "aws_db_subnet_group" "rdsSubnet" {
  name       = "main_subnet"
  subnet_ids = ["${aws_subnet.ec2-mysql-Subnet.id}", "${aws_subnet.rdsSubnettwo.id}"]
}

## Subnet ec2-mysql
resource "aws_subnet" "ec2-mysql-Subnet" {
  availability_zone = "eu-west-1a"
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.3.0/24"
}

## RDS
resource "aws_db_instance" "rds" {
  identifier           = "pythondb"
  allocated_storage    = 10
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  name                 = "mydb"
  username             = "foo"
  password             = "foobarbaz"
  parameter_group_name = "default.mysql5.7"
  port                 = 3306
  skip_final_snapshot  = true
  publicly_accessible  = true
  vpc_security_group_ids = [aws_security_group.ec2-mysql.id]
  db_subnet_group_name = aws_db_subnet_group.rdsSubnet.id
}

## Template file
resource "template_file" "python-script" {
    template = "ec2write.py"
}

## EC2
resource "aws_instance" "ec2"{
  ami                         = "ami-0701e7be9b2a77600"
  instance_type               = "t2.micro"
  key_name                    = "key_pair_instance"
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.ec2-mysql.id]
  subnet_id                   = aws_subnet.ec2-mysql-Subnet.id

  user_data                   = <<-EOF
                                #!/bin/bash
                                sudo apt-get update
                                sudo apt-get upgrade -y
                                sudo apt install python3-pip -y
                                pip3 install --upgrade pip
                                pip3 install web3==5.7.0
                                pip3 install threaded==4.0.8
                                pip3 install pandas==1.0.1
                                pip3 install PyMySQL==0.9.3
                                pip3 install requests==2.20.1
                                EOF
}

resource "aws_eip" "elasticip" {
  vpc      = true
  instance = aws_instance.ec2.id
}

/*
resource "tls_private_key" "privateKey" {
  algorithm = "RSA"
  rsa_bits  = 4096
}*/

/*resource "aws_key_pair" "keypair" {
  key_name   = "key_pair_instance"
  public_key = tls_private_key.privateKey.public_key_openssh
}*/

## Security Group ec2
resource "aws_security_group" "ec2-mysql"{
  name = "security_group_ec2-mysql"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    description = "Telnet"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    description = "HTTP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    description = "HTTPS"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress{
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    description = "Mysql"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic.
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "public_ip" {
  value       = aws_instance.ec2.public_ip
  description = "the public ip of the server"
}

## put as outputs the endpoints