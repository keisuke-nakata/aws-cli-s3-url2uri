# -*- coding: utf-8 -*-

import re
import subprocess

import click

REGEXP = r'https://.+&bucket=(?P<bucket>.*)&prefix=(?P<prefix>.*)'
S3URI_FORMAT = 's3://{bucket}/{prefix}'


def url2uri(url):
    """
    convert URL to s3 uri

    - Bucket root
    "https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix="
    ->
    "s3://mybucket/"

    - Top layer directory
    "https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix=mydir/"
    ->
    "s3://mybucket/mydir/"

    - Nested directory
    "https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix=mydir/nested/"
    ->
    "s3://mybucket/mydir/nested/"
    """
    match = re.match(REGEXP, url)
    if not match:  # does not match S3 url
        return url
    groupdict = match.groupdict()  # {'bucket': ..., 'prefix': ...}
    s3uri = S3URI_FORMAT.format(**groupdict)
    return s3uri


@click.command(context_settings={'ignore_unknown_options': True})
@click.argument('subcommand', type=click.Choice(['ls', 'rm', 'cp', 'mv', 'sync', 'presign']))
@click.argument('args', nargs=-1)
def awscli_s3_url2uri(subcommand, args):
    """Entry point"""
    uried_args = [url2uri(arg) for arg in args]
    command = ['aws', 's3', subcommand] + uried_args
    print(' '.join(command))
    _ = subprocess.call(command)
