import boto3

#add a try catch for error of user was already created
print('This is a function to create users.\n')
print('Tell me the name of the user:')
username = input(int())


def createUser(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print('User ' + username + ' has been created succesfully.')

createUser(username)