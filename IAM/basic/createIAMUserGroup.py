import boto3

def createGroup(group_name):
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)

createGroup('Admins')