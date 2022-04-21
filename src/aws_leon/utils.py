import boto3


def get_default_region():
    return boto3.session.Session().region_name or ""
