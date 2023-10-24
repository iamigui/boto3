import boto3
from colorama import init, Fore, Back, Style
import sys

def createUser(username):
    iam = boto3.client('iam')
    try:
        response = iam.create_user(UserName=username)
        print('User ' + username + ' has been created succesfully.')

    except Exception as e:
        print(Fore.RED +'An error occurred:', e)
        sys.exit(1)


def checkUser():
    try:
        print('Insert the name of the user: ')
        iam = boto3.client('iam')
        global username
        username = input()
        username_encontrada = False
        paginator = iam.get_paginator('list_users')

        for response in paginator.paginate():
            for user in response['Users']:
                if username == user['UserName']:
                    arn = user['Arn']
                    print(Fore.GREEN + '\nThe username: ' + username + ' exists.')
                    username_encontrada = True
                    break

        if not username_encontrada:
            print('\nUnknown user. Do you want to create it? y/n: ')
            response = input()
            if response == 'y':
                createUser(username)
            elif response == 'n':
                sys.exit(1)
            else:
                sys.exit(1)
    
    except Exception as e:
        print('An error occurred:', e)
        sys.exit(1)


if __name__ == "__main__":
    print('This is a function to create users.\n')
    
    checkUser()