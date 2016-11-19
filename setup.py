# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pip.req import parse_requirements

with open('README.md') as f:
    long_description = f.read()

install_requires = [
    str(pr.req) for pr in parse_requirements('requirements.txt', session='hack')
]


setup(
    name='aws_s3_url2uri',
    description='Make awscli s3 commands work with URL',
    long_description=long_description,
    version='0.1.3',
    author='NAKATA Keisuke',
    author_email='keisuke.nakata.919@gmail.com',
    url='https://github.com/keisuke-nakata/aws-cli-s3-url2uri',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=install_requires,
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'aws_s3_url2uri=aws_s3_url2uri.main:aws_s3_url2uri'
        ]
    }
)
