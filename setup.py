# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pip.req import parse_requirements


install_requires = [
    str(pr.req) for pr in parse_requirements('requirements.txt', session='hack')
]


setup(
    name='aws_s3_url2uri',
    description='Make awscli s3 commands work with URL',
    version='0.1',
    packages=find_packages(),
    install_requires=install_requires,
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'aws_s3_url2uri=aws_s3_url2uri.main:aws_s3_url2uri'
        ]
    }
)
