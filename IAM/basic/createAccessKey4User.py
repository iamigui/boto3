import boto3

#Añadirlo al script grande con check de usuario

def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)

create_access('testuser')

def update_access():
    iam = boto3.client('iam')
    accesskey = input("Dime tu access key: ")
    status = input("Dime el status de tu AccessKey: ")
    username = input("Username: ")
    iam.update_access_key(
        AccessKeyId=accesskey,
        Status=status,
        UserName=username
    )

    print(f'The user ${username} with AccessKey defined is in status ${status}')

update_access()