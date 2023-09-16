import boto3

print('This is a function to attach policies to users.\n')
print('Tell me the name of the user:')
username = input(int())

def listPolicies():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_policies')
    print('Para esto necesitas saber el ARN de la policy que buscas...')
    print('¿Sabes el nombre de la policy que buscas?: y/n ')
    respuesta = input()
    if respuesta == 'y':
        print('Dime el nombre de la policy: ')
        policy_name = input()
        for response in paginator.paginate(Scope='AWS'):
            for policy in response['Policies']:
                if policy_name in policy['PolicyName']:
                    Arn = policy['Arn']
                    print('Policy Name : {} Arn : {}'.format(policy_name, Arn))
                    break
                else:
                    print('Nombre de policy desconocido.')
                    break
            break

    elif respuesta == 'n' :
        print('This is the list of policies from AWS:')
        for response in paginator.paginate(Scope="AWS"): #The scope can be changed to the customer, Local or AWS to list all policies
            for policy in response['Policies']:
                policy_name = policy['PolicyName']
                Arn = policy['Arn']

                print('Policy Name : {} Arn : {}'.format(policy_name, Arn))

listPolicies()

def attachPolicy(policy_arn, username):
    iam = boto3.client('iam')

    input('Dime el policy ARN: ')
    response = iam.attach_user_policy(
        UserName = username,
        PolicyArn = policy_arn
    )

    print('The policy ' + policy_name + ' has been attached to the user: ' + username)

attachPolicy(policy_arn, username)
