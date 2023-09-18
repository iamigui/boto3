import boto3

def addUser(username, group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName = username,
        GroupName = group_name
    )

    print('The user: ' + username + ' has been added to group: ' + group_name)

addUser('papafrita', 'Admins')