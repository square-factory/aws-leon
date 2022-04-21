from setuptools import setup, find_packages


setup(
    name="aws-leon",
    author="square-factory",
    author_email="contact@square-factory.io",
    url="https://github.com/square-factory/aws-leon",
    description="AWS AMI cleaner",
    license="MIT",
    keywords=["aws", "ami", "cleaning", "snapshot", "finops"],
    classifiers=["Programming Language :: Python :: 3.8"],
    entry_points={"console_scripts": ["aws-leon=aws_leon.main:main"]},
    zip_safe=True,
    include_package_data=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "boto3>=1.21",
        "click>=8.1",
        "rich>=12.2",
    ],
)
