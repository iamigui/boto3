import boto3
import json
import datetime
import time

def create_role():
    iam = boto3.client('iam')

    role_name = input("Tell me the Role Name you want to give: ")

    json_file = str(input("Tell me the complete route of the json file: "))

    with open(json_file, 'r') as policy_document:
        policy_document_content = policy_document.read()

    iam.create_role(
        RoleName = role_name,
        AssumeRolePolicyDocument = policy_document_content
    )

    print(f"IAM Role {role_name} created!")

def create_policy():
    iam = boto3.client('iam')

    policy_name = input("Tell me the Policy Name you want to give: ")

    json_file = str(input("Tell me the complete route of the json file: "))

    with open(json_file, 'r') as policy_document:
        policy_document_content = policy_document.read()

    iam.create_policy(
        PolicyName=policy_name,
        PolicyDocument=policy_document_content
    )

    print(f"IAM Policy {policy_name} has been created")

def attach_policy():

    iam = boto3.client('iam')

    role_name = input("Dime el nombre del rol: ")

    policy_name = input("Dime el nombre de la policy: ")

    iam.attach_role_policy(
        RoleName = role_name,
        PolicyArn = ""#Añadir policy arn del policy ya creado
    )

    print(f"Policy {policy_name} attached to IAM Role {role_name}")

def create_instance_profile():
    iam = boto3.client('iam')

    instance_profile_name = input("Tell me the instance profile name: ")

    iam.create_instance_profile(
        InstanceProfileName = instance_profile_name
    )

    print(f"Instance profile created {instance_profile_name}")

def add_role_to_iam_instance():
    iam = boto3.client('iam')

    role_name = input("Dime el nombre del rol: ")

    instance_profile_name = input("Tell me the instance profile name: ")

    iam.add_role_to_permissions(
        InstanceProfileName=instance_profile_name,
        RoleName=role_name
    )

    print(f"IAM Role {role_name} added to IAM instance profile {instance_profile_name}")

def tag_users():
    iam_client = boto3.client('iam')

    num = int(input("How many users you want to tag the same?: "))
    key = input("Tell me the name of the key: ")
    value = input("Tell me the name of the value: ")
    tags = [{'Key':key, 'Value':value}, {'Key':'Project', 'Value':'Onboarding'}]

    i=0
    while (i < num):
        user_name = input("Tell me the username: ")
        iam_client.tag_user(UserName=user_name, Tags=tags)
        print(f"The user {user_name} has been tagged {key}:{value}")
        i+=1

def list_tags():
    iam_client = boto3.client('iam')

    response = iam_client.list_users()

    for user in response['Users']:
        user_name = user['UserName']
        tags = iam_client.list_user_tags(UserName=user_name)['Tags']
        print(F"The user: {user}, Tags: {tags}")

def remove_tag():
    iam_client = boto3.client('iam')

    print("You are going to tag a user in this format: Key:Value")
    time.sleep(5)

    user_name = input("Tell me the username: ")
    key = input("Tell me the name of the key: ")

    tag_keys = [key]

    iam_client.untag_user(UserName=user_name, TagKeys=tag_keys)

    print(f"The user {user_name} has been untagged from the key: {key}")

def create_conditional_policies():
    iam = boto3.client('iam')

    current_date = datetime.utcnow().strftime('%Y-%m-%d')

    start_time = f"{current_date}T01:00:00Z"
    end_time = f"{current_date}T03:00:00Z"

    policy_name = input("Tell me the Policy Name you want to give: ")

    policy_document = {
        "Version":"2012-10-17",
        "Statement": [
            { 
                "Effect":"Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::mybucket/*", #Cambiar por tu bucketname
                "Condition": {
                    "DateGreaterThan": {"aws:CurrentTime": start_time},
                    "DateLessThan": {"aws:CurrentTime": end_time}
                }
            }
        ]
    }

    iam.create_policy(
        PolicyName=policy_name,
        PolicyDocuemt=json.dumps(policy_document)
    )

    print(f"IAM Policy {policy_name} has been created")

def list_amis():
    # Crea un cliente de EC2 utilizando Boto3
    ec2_client = boto3.client('ec2')

    # Obtiene todas las AMIs en la región por defecto
    response = ec2_client.describe_images(Owners=['amazon'])

    # Imprime información sobre cada AMI
    for ami in response['Images']:
        print(f"ID: {ami['ImageId']}")
        print(f"Nombre: {ami.get('Name', 'N/A')}")
        print(f"Descripción: {ami.get('Description', 'N/A')}")
        print(f"Tipo de Arquitectura: {ami.get('Architecture', 'N/A')}")
        print(f"Tipo de Plataforma: {ami.get('Platform', 'N/A')}")
        print(f"-------------------------------------")

def create_ec2_with_instanceprofile():
    ec2_client = boto3.client('ec2')

    instance_profile_name = input("Tell me the instance profile name: ")

    ami_id = input("Tell me the AMI ID: ")
    instance_type = input("Tell me the Instance Type: ")

    response = ec2_client.run_instances (
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        IamInstanceProfile={
            'Name': instance_profile_name
        }
    )

    instance_id = response['Instances'][0]['InstanceId']
    print(f"EC2 instance with IAM Instance Profile {instance_profile_name} launched. Instance ID: {instance_id}")

print('Select what you want to do:\n')
print('1) Create Role: ')
print('2) Create Policy: ')
print('3) Attach Policy to Role: ')
print('4) Create Instance Profile: ')
print('5) Add role to IAM instance: ')
print('6) Create Conditional Policies: ')
print('7) Tag User: ')
print('8) List Tag: ')
print('9) Remove Tag: ')
print('10) List EC2 AMIs: ')
print('11) Create EC2 with Instance Profile: \n')
response = input()

if (response == "1"):
    create_role()
elif (response == "2"):
    create_policy()
elif (response == "3"):
    attach_policy()
elif (response == "4"):
    create_instance_profile()
elif (response == "5"):
    add_role_to_iam_instance()
elif (response == "6"):
    create_conditional_policies()
elif (response == "7"):
    tag_users()
elif (response == "8"):
    list_tags()
elif (response == "9"):
    remove_tag()
elif (response == "10"):
    list_amis()
elif (response == "11"):
    create_ec2_with_instanceprofile()
else:
    print("Not found")