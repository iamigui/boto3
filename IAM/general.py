import boto3
from datetime import datetime
import os
import json
from colorama import init, Fore, Back, Style
import sys

#---------------------------------------------------------------------------------------------

init(autoreset=True)

def checkUser():
    try:
        print('Insert the name of the user: ')
        iam = boto3.client('iam')
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
            print(Fore.RED + '\nUnknown user.')
            sys.exit(1)
    
    except Exception as e:
        print(Fore.RED +'An error occurred:', e)

def listPolicies():
        try:
            iam = boto3.client('iam')
            policy_encontrada = False
            paginator = iam.get_paginator('list_policies')
            print('I need to know the ARN from the policy you look for...')
            print('Select how you want to display the policies:\n')
            print('1) Verify the policy ARN: ')
            print('2) List all policies: ')
            print('3) Check the policies that contain the text: \n')

            respuesta = input()
            
            if respuesta == '1':
                print('Tell me the name of policy: ')
                global policy_name
                policy_name = input(str())
                for response in paginator.paginate(Scope='All'):
                    for policy in response['Policies']:
                        if policy_name == policy['PolicyName']:
                            Arn = policy['Arn']
                            print('Policy Name : {} Arn : {}'.format(policy_name, Arn))
                            policy_encontrada = True
                            break

                if not policy_encontrada:
                    print('Unknown policy name.\n')

            elif respuesta == '2' :
                print('This is the list of policies from AWS:')
                for response in paginator.paginate(Scope="AWS"): #The scope can be changed to the customer, Local or AWS to list all policies
                    for policy in response['Policies']:
                        policy_name = policy['PolicyName']
                        Arn = policy['Arn']

                        print('Policy Name : {} Arn : {}'.format(policy_name, Arn))

            elif respuesta == '3':
                print('Tell me the name of policy: ')
                policy_name = input(str())
                for response in paginator.paginate(Scope='All'):
                    for policy in response['Policies']:
                        if policy_name in policy['PolicyName']:
                            Arn = policy['Arn']
                            print('Policy Name : {} Arn : {}'.format(policy['PolicyName'], Arn))
                            policy_encontrada = True
                            break

                if not policy_encontrada:
                    print(Fore.RED +'Unknown policy name.')

            else:
                print(Fore.RED +'\nNot valid option.')

        except Exception as e:
            print(Fore.RED +'An error occurred:', e)
            sys.exit(1)

def attachPolicy(policy_arn, username):
    try:
        iam = boto3.client('iam')

        response = iam.attach_user_policy(
            UserName = username,
            PolicyArn = policy_arn
        )

        print(Fore.GREEN + 'The policy ' + policy_name + ' has been attached to the user: ' + username)
    
    except Exception as e:
        print(Fore.RED +'An error occurred:', e)
        sys.exit(1)

def detachPolicy(arn, username):
    try:
        iam = boto3.client('iam')

        response = iam.detack_user_policy(
            UserName = username,
            PolicyArn = policy_arn
        )

        print(Fore.GREEN + 'The policy ' + policy_name + ' has been detached from the user: ' + username)
    
    except Exception as e:
        print(Fore.RED +'An error occurred:', e)
        sys.exit(1)

if __name__ == "__main__":
    print('This is a function to attach policies to users.\n')
    checkUser()

    listPolicies()

    print('Insert the policy ARN: ')
    policy_arn = input()

    attachPolicy(policy_arn, username)

#---------------------------------------------------------------------------------------------

def createUser():
    username = input("Tell me the username: ")

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

def createGroup():
    group_name = input("Tell me the Group Name: ")
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)

def addUserToGroup():

    username = input("Tell me the username: ")
    group_name = input("Tell me the Group Name: ")

    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName = username,
        GroupName = group_name
    )

    print('The user: ' + username + ' has been added to group: ' + group_name)

def attachPolicyUserGroup():

    policy_arn = input("Tell me the Policy ARN: ")
    group_name = input("Tell me the Group Name: ")

    iam = boto3.client('iam')
    response = iam.attach_group_policy(
        GroupName = group_name,
        PolicyArn = policy_arn
    )

    print('The policy: ' + policy_arn + ' has been attached to the user group: ' + group_name)

def createLoginProfile():
    username = input("Tell me the username you want to create a Login Profile: ")
    iam = boto3.client('iam')

    login_profile = iam.create_login_profile(
        Password = 'Mypassword@1',
        PasswordResetRequired = False,
        UserName = username
    )

    print(login_profile)

def deleteUser():
    username = input("Tell me the username you want to delete: ")
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName = username
    )

    print(f'The user {username} has been deleted')

def deleteUserFromGroup():
    print("This is a function to delete Users from Groups")
    username = input("Tell me the user: ")
    groupName = input("Tell me the group: ")
    iam = boto3.client('iam')

    group = iam.Group(groupName)

    response = group.remove_user(
        UserName = username
    )

    print(f'The user {username} has been removed from Group: {groupName}')

#---------------------------------------------------------------------------------------------

def createAccessKey():
    username = input("Tell me the username to create an Access Key: ")

    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(f"Access Key created for User: {username} with the Response {response}")

def updateAccessKey():
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

#---------------------------------------------------------------------------------------------

def detachPolicyFromUserGroup():
    user_group = input("Tell me the User Group: ")
    arn = input("Tell me the ARN of the policy: ")

    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        UserGroup=user_group,
        PolicyArn = arn
    )

    print(response)

#---------------------------------------------------------------------------------------------

def allUsers():
    iam = boto3.client('iam')
    while True:
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

def updateUser():

    old_username = input("Tell me the old username: ")
    new_username = input("Tell me the new username: ")
    iam = boto3.client('iam')

    response = iam.update_user(
        UserName = old_username,
        NewUserName = new_username
    )

    print('The user ' + old_username + ' has been renamed to: ' + new_username)