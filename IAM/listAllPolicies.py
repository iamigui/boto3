import boto3

def listPolicies():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="Local"): #The scope can be changed to the customer or AWS to list all policies
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            Arn = policy['Arn']

            print('Policy Name : {} Arn : {}'.format(policy_name, Arn))

listPolicies()