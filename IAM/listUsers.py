import boto3

def allUsers():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            arn = user['Arn']
            print('The username: ' + username + ' has the arn ' + arn)

allUsers()