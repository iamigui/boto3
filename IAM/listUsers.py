import boto3
from colorama import init, Fore, Back, Style

init(autoreset=True)

def allUsers():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')

    print('Select how you want to display the users:\n')
    print('1) List all users: ')
    print('2) Verify if an user exists: ')
    print('3) Check user ARN: \n')

    eleccion = input()

    if eleccion == '1':
        print('You chose to list all users:\n')
        for response in paginator.paginate():
            for user in response['Users']:
                username = user['UserName']
                arn = user['Arn']
                print(Fore.GREEN + '\nThe username: ' + username + ' has the arn ' + arn)
    
    elif eleccion == '2':
        print('\nInsert the username: ')
        username = input()

        username_encontrada = False

        for response in paginator.paginate():
            for user in response['Users']:
                if username == user['UserName']:
                    arn = user['Arn']
                    print(Fore.GREEN + '\nThe username: ' + username + ' exists.')
                    username_encontrada = True
                    break

        if not username_encontrada:
            print(Fore.RED + '\nUnknown user.')
    
    elif eleccion == '3':
        print('\nInsert the username: ')
        username = input()

        username_encontrada = False

        for response in paginator.paginate():
            for user in response['Users']:
                if username == user['UserName']:
                    arn = user['Arn']
                    print(Fore.GREEN + '\nThe username: ' + username + ' has the arn ' + arn)
                    username_encontrada = True
                    break

        if not username_encontrada:
            print(Fore.RED + '\nUnknown user.')

allUsers()