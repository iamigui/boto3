import boto3

def attachPolicyUserGroup(policy_arn, group_name):
    iam = boto3.client('iam')
    response = iam.attach_group_policy(
        GroupName = group_name,
        PolicyArn = policy_arn
    )

    print('The policy: ' + policy_arn + ' has been attached to the user group: ' + group_name)

attachPolicyUserGroup('arn:aws:iam::aws:policy/ReadOnlyAccess', 'Admins')