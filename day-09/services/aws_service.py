import boto3
import json
import datetime

def datetime_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def get_aws_resource():
    s3_client=boto3.client('s3')
    ec2_client=boto3.client('ec2')

    report_data={
        "s3_bucket":[],
        "ec2_instance":[]
    }

    try:
        s3_responce=s3_client.list_buckets()

        if 'Buckets' in s3_responce:
            for bucket in s3_responce['Buckets']:
                bucket_name=bucket['Name']
                report_data["s3_bucket"].append(bucket_name)
                print(f"bucket found:{bucket_name}")
        else:
            print(f"No bucket found")
    except Exception as e:
        print(f"Error fetchiung s3 buckets: {e}")
    
    try:
        ec2_reponse=ec2_client.describe_instances()
        # print(ec2_reponse)
        for reservation in ec2_reponse['Reservations']:
            for instance in reservation['Instances']:
                instance_info={
                    "InstanceId": instance.get('InstanceId'),
                    "InstanceType": instance.get('InstanceType'),
                    "State": instance['State']['Name'],
                    "LaunchTime": instance.get('LaunchTime')
                }
                report_data['ec2_instance'].append(instance_info)
                # print(f"Found EC2 {instance_info['InstanceId']} {instance_info['State']}")

    except Exception as e:
        print(f"Error fetchiung ec2 instance: {e}")

    return report_data


