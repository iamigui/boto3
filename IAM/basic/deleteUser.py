import boto3

user = input("Tell me the user to delete: ")

def delete_user(username):
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName = username
    )

    print(response)

delete_user(user)