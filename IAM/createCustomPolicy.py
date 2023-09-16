import boto3
import json

#Para mejorarlo, pasar en input un archivo json en el que venga el policy que quieras y su nombre
def createAdminPolicy():
    iam = boto3.client('iam')

    name_policy = 'adminPolicy'
    user_policy = {
        "Version":"2012-10-17",
        "Statement":[
            {
            "Effect":"Allow",
            "Action":"*",
            "Resource": "*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName = name_policy,
        PolicyDocument = json.dumps(user_policy)
    )

    print('The policy ' + name_policy + ' has been created successfully')

createAdminPolicy()