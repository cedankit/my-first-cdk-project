import enum
from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as _s3,



    # aws_sqs as sqs,
)
from constructs import Construct


class MyFirstProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="cdk-ankit-35",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )

        # example resource
        # queue = sqs.Queue(
        #     self, "MyFirstProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
