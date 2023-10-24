import boto3

def updateUser(old_username, new_username):
    iam = boto3.client('iam')

    response = iam.update_user(
        UserName = old_username,
        NewUserName = new_username
    )

    print('The user ' + old_username + ' has been renamed to: ' + new_username)

updateUser('elenita', 'elenitaa')