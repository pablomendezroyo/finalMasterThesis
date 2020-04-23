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

## Route Table
resource "aws_route_table" "r" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.gw.id}"
  }
}

## Route table association
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.instanceSubnet.id
  route_table_id = aws_route_table.r.id
}

## Subnet rds1
resource "aws_subnet" "rdsSubnetone" {
  availability_zone = "eu-west-1a"
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
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
  subnet_ids = ["${aws_subnet.rdsSubnetone.id}", "${aws_subnet.rdsSubnettwo.id}"]
}

## Subnet ec2
resource "aws_subnet" "instanceSubnet" {
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
  skip_final_snapshot  = true
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name = aws_db_subnet_group.rdsSubnet.id
}

## EC2
resource "aws_instance" "ec2"{
    ami                         = "ami-0f2ed58082cb08a4d"
    instance_type               = "t2.micro"
    key_name                    = "key_pair_instance"
    associate_public_ip_address = true
    vpc_security_group_ids      = [aws_security_group.instance.id]
    subnet_id                   = aws_subnet.instanceSubnet.id
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
resource "aws_security_group" "instance"{
  name = "security_group_instance"
  vpc_id = aws_vpc.main.id

  ##need to put the rds 

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

  # Allow all outbound traffic.
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

## Security Group db
resource "aws_security_group" "rds"{
  name = "security_group_rds"
  vpc_id = aws_vpc.main.id

  ingress {
      from_port = 0
      to_port = 65535
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
      from_port = 0
      to_port = 65535
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
}
}

output "public_ip" {
  value       = aws_instance.ec2.public_ip
  description = "the public ip of the server"
}