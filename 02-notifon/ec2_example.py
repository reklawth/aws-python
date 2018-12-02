# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name +'.pem'
key = ec2.create_key_pair(keyName=key_name)
key = ec2.create_key_pair(KeyName=key_name)
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-09479453c5cde9639')
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20181116-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img
key
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceTyper='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
inst = instances[0]
inst.terminate()
ec2.describe_instances()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.reload()
inst.public_dns_name
# Look up the security group
# Authorize incoming connection from public IP address on port 22 for SSH
sg = ec2.SecurityGroups(inst.security_groups[0]['GroupId'])
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort: 22, 'IpProtocol: 'TCP', 'IpRanges': [{'CidrIp': '162.233.171.126/32}]}])
sg.authorize_security_group_ingress(IpPermissions=[{'FromPort': 22, 'ToPort: 22, 'IpProtocol: 'TCP', 'IpRanges': [{'CidrIp': '162.233.171.126/32}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '162.233.171.126/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '108.48.120.175/32'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
