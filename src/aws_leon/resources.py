import boto3
import logging
from .config import Config
from botocore.config import Config as BotoConfig


class AMI:
    def __init__(self) -> None:
        boto3.set_stream_logger(name="botocore.credentials", level=logging.WARNING)
        self.ec2 = boto3.client("ec2", config=BotoConfig(retries={"max_attempts": 10}))

    def filter(self, config: Config) -> dict:
        available_amis = dict()
        custom_images = self.ec2.describe_images(Owners=["self"])
        for image_json in custom_images.get("Images"):
            available_amis[image_json.get("ImageId")] = dict(
                name=image_json.get("Name"),
                creation_date=image_json.get("CreationDate"),
            )
        return available_amis
