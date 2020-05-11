import boto3
import sys

def change_status(region, status_now, status_todo):
    ec2 = boto3.resource('ec2', region_name=region)
    responce = ec2.instances.all()
    for instance in responce:
        print(instance.id, instance.state)
        if instance.id is None:
            instance = ec2.create_instances(
                ImageId='ami-0323c3dd2da7fb37d',
                MinCount=1,
                MaxCount=1,
                InstanceType='t2.micro')
        for status_now in instance.state:
            if status_now == 'stopped' and status_todo is not ['stopped']:
                continue
            if status_now == 'running' and status_todo is not ['started']:
                continue
            if status_now == 'terminated':
                print('You can change status')
                sys.exit()
            if status_todo == 'stopped':
                ec2.Instance(instance.id).stop()
            elif status_todo == 'running':
                ec2.Instance(instance.id).start()
            elif status_todo == 'reboot':
                ec2.Instance(instance.id).reboot()
            elif status_todo == 'terminated':
                ec2.Instance(instance.id).terminate()

