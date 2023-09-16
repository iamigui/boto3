import boto3

policy_name = 0

def listPolicies():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_policies')
    print('Para esto necesitas saber el ARN de la policy que buscas...')
    print('¿Sabes el nombre de la policy que buscas?: y/n ')
    respuesta = input()
    if respuesta == 'y':
        print('Dime el nombre de la policy: ')
        policy_name = input()
        for response in paginator.paginate(Scope='All'):
            for policy in response['Policies']:
                Arn = policy['Arn']
                print('Policy Name : {} Arn : {}'.format(policy_name, Arn))

listPolicies()
