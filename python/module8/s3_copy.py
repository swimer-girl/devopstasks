import boto3

def copy_file_between_s3(new_bucket, use_bucket):
    s3 = boto3.resource('s3')

    for bucket in s3.buckets.all():
        bucketlist = [bucket.name]
        print(bucket.name)

    if new_bucket not in bucketlist:
        s3.create_bucket(Bucket=new_bucket)
        new_bucket = s3.Bucket(new_bucket)
        print(f"Created {new_bucket.name} bucket")
        new_bucket = new_bucket.name

    new_bucket = s3.Bucket(new_bucket)
    use_to_copy = s3.Bucket(use_bucket)
    for file in use_to_copy.objects.all():
        use_file = {'Bucket': use_bucket,
                    'Key': file.key}
        new_bucket.copy(use_file, file.key)
