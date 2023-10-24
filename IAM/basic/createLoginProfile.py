import boto3

def create_login(username):
    iam = boto3.client('iam')

    login_profile = iam.create_login_profile(
        Password = 'Mypassword@1',
        PasswordResetRequired = False,
        UserName = username
    )

    print(login_profile)

create_login('test')
