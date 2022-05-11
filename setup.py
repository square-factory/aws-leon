from setuptools import setup, find_packages


setup(
    name="aws-leon",
    author="sq4",
    author_email="contact@sq4.io",
    url="https://github.com/square-factory/aws-leon",
    description="AWS AMI cleaner",
    license="MIT",
    keywords=["aws", "ami", "cleaning", "snapshot", "finops"],
    classifiers=["Programming Language :: Python :: 3.9"],
    entry_points={"console_scripts": ["aws-leon=aws_leon.main:main"]},
    zip_safe=True,
    include_package_data=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "boto3",
        "click==8.0.4",
        "rich",
    ],
)
