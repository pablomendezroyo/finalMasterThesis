Basic EC2 instance
Configuration in this directory creates EC2 instances with different sets of arguments (with Elastic IP, with network interface attached, with credit specifications).

Usage
To run this example you need to execute:

$ terraform init
$ terraform plan
$ terraform apply
Note that this example may create resources which can cost money. Run terraform destroy when you don't need these resources.

Outputs
Name	Description
credit_specification	Credit specification of EC2 instance (empty list for not t2 instance types)
credit_specification_t2_unlimited	Credit specification of t2-type EC2 instance
ebs_block_device_volume_ids	List of volume IDs of EBS block devices of instances
ids	List of IDs of instances
ids_t2	List of IDs of t2-type instances
instance_id	EC2 instance ID
instance_public_dns	Public DNS name assigned to the EC2 instance
placement_group	List of placement group
public_dns	List of public DNS names assigned to the instances
root_block_device_volume_ids	List of volume IDs of root block devices of instances
t2_instance_id	EC2 instance ID
tags	List of tags
vpc_security_group_ids	List of VPC security group ids assigned to the instances