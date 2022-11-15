# import boto3

# # ec2 = boto3.resource('ec2', region='us-east-1')
# ec2 = boto3.resource('ec2')
# security_group = ec2.SecurityGroup('sg-0d259d174ffdb9e11')
# rules = security_group.ip_permissions
# # print (rules)
# for rule in rules:
#     for sourcerange in rule['IpRanges']:
#         if sourcerange['CidrIp'] == '0.0.0.0/0':
#             # print ("Remove the rule")
#             security_group.revoke_ingress(IpPermissions=[rule])
#             print ("The open Inbound Rule in the Security Group ID:  {} Rule:  {}".format(security_group.group_id, rule))
#         else:
#             print ("Rules are as per standard")

#Transform the above code to have functions and modules

# For one Particular security_group
# import boto3

# # ec2 = boto3.resource('ec2', region='us-east-1')
# ec2 = boto3.resource('ec2')
# security_group = ec2.SecurityGroup('sg-0d259d174ffdb9e11')
# rules = security_group.ip_permissions
# # print (rules)
# def check_rules():
#     for rule in rules:
#         for sourcerange in rule['IpRanges']:
#             if sourcerange['CidrIp'] == '0.0.0.0/0':
#                 # print ("Remove the rule")
#                 security_group.revoke_ingress(IpPermissions=[rule])
#                 print ("DELETED: Security Group ID:  {} Rule:  {}".format(security_group.group_id, rule))
#             else:
#                 print ("Rules are as per standard")
# check_rules()






import boto3

# ec2 = boto3.resource('ec2', region='us-east-1')
ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups()
def check_rules():
    for sg_list in response['SecurityGroups']:\
        sg_list = sg_list['GroupId']
        sg = ec2_resource.SecurityGroup(sg_id)
        rules = sg.ip_permissions
        for rule in rules:
            for sourcerange in rule['IpRanges']:
                if sourcerange['CidrIp'] == '0.0.0.0/0':
                    # print ("Remove the rule")
                    security_group.revoke_ingress(IpPermissions=[rule])
                    print ("DELETED: Security Group ID:  {} Rule:  {}".format(sg.group_id, rule))
                else:
                    print ("Rules are as per standard")
check_rules()
















# Final one below for all SG

# import boto3
# ec2_resource = boto3.resource('ec2') 
# ec2_client = boto3.client('ec2')
# response = ec2_client.describe_security_groups()
# def check_rules():
#     for sg_list in response['SecurityGroups']:
#         sg_id = sg_list['GroupId']
#         sg = ec2_resource.SecurityGroup(sg_id)
#         rules = sg.ip_permissions
#         for rule in rules:
#             for sourcerange in rule['IpRanges']:
#                 if sourcerange['CidrIp'] == '0.0.0.0/0':
#                     sg.revoke_ingress(IpPermissions=[rule])
#                     print ("DELETED: Security Group ID:  {} Rule:  {}".format(sg.group_id, rule))
#                 else:
#                     print ("Rules are as per standards")
# check_rules()