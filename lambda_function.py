import boto3
from botocore.exceptions import ClientError


def check_s3_buckets():
    s3 = boto3.client("s3")
    region_name = "us-east-1"
    sns = boto3.client("sns", region_name=region_name)
    topic_arn = "arn:aws:sns:us-east-1:730335381060:S3SecurityAlerts"  # Update with your SNS Topic ARN

    # List all S3 buckets
    buckets = s3.list_buckets()

    for bucket in buckets["Buckets"]:
        bucket_name = bucket["Name"]

        try:
            # Get the bucket's ACL
            acl = s3.get_bucket_acl(Bucket=bucket_name)

            # Attempt to get the bucket policy status
            try:
                public_access_block = s3.get_bucket_policy_status(Bucket=bucket_name)
            except ClientError as e:
                # Check if the error is due to the absence of a bucket policy
                if e.response["Error"]["Code"] == "NoSuchBucketPolicy":
                    public_access_block = None  # No policy exists, set to None
                    print(
                        f"No bucket policy for {bucket_name}, proceeding with ACL check."
                    )
                else:
                    print(f"Error checking bucket policy for {bucket_name}: {e}")
                    continue  # Skip to the next bucket

            # Check if the bucket has public access
            is_public = any(
                "URI" in grant.get("Grantee", {})
                and grant["Grantee"]["URI"]
                == "http://acs.amazonaws.com/groups/global/AllUsers"
                for grant in acl["Grants"]
            )

            if is_public:
                message = f"Alert: Bucket {bucket_name} is publicly accessible!"
                print(message)

                # Publish alert to SNS
                sns.publish(
                    TopicArn=topic_arn,
                    Message=message,
                    Subject="S3 Bucket Misconfiguration Alert",
                )
            else:
                print(f"Bucket {bucket_name} is secure.")

        except Exception as e:
            print(f"Error checking bucket {bucket_name}: {e}")


if __name__ == "__main__":
    check_s3_buckets()
