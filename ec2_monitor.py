import boto3
from botocore.exceptions import ClientError

REGION = 'us-east-1'

def run_ec2_report():
    try:
        ec2_client = boto3.client('ec2', region_name = REGION)
        response = ec2_client.describe_instances()
        if not response['Reservations']:
            print('No instances found!')
            return

        reservation = response['Reservations']
        for reserve in reservation:
            instance = reserve['Instances']

            for insta in instance:
                instance_name = ''
                tag_list = insta.get('Tags', [])
                for tags in tag_list:
                    if tags['Key'] == 'Name':
                        instance_name= tags['Value']
                        break
                print(f"InstanceID: {insta['InstanceId']}, Name of state: {insta['State']['Name']}, Name tag: {instance_name} ")
    except Exception as e:
        print(f'The error in this code is {e}!')

run_ec2_report()