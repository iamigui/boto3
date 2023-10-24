import boto3

user = input("Tell me the user: ")
group = input("Tell me the group: ")

def delete_user_group(username, groupName):
    iam = boto3.client('iam')

    group = iam.Group(groupName)

    response = group.remove_user(
        UserName = username
    )

    print(response)

delete_user_group(user, group)