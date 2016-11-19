# coding=utf-8

import unittest

from aws_s3_url2uri.main import url2uri


class TestURL2URI(unittest.TestCase):
    def test_bucket_root(self):
        """bucket root URL shold be converted to URI"""
        url = 'https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix='
        actual = url2uri(url)
        expected = 's3://mybucket/'
        self.assertEqual(actual, expected)

    def test_top_layer_directory(self):
        """top layer directory shold be converted to URI"""
        url = 'https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix=mydir/'
        actual = url2uri(url)
        expected = 's3://mybucket/mydir/'
        self.assertEqual(actual, expected)

    def test_nested_directory(self):
        """nested directory shold be converted to URI"""
        url = 'https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix=mydir/nested/'
        actual = url2uri(url)
        expected = 's3://mybucket/mydir/nested/'
        self.assertEqual(actual, expected)

    def test_non_url_untouched(self):
        """If parameter does not start with 'https://' it shold not be converted"""
        non_url = '/home/myname/tmp/dir'
        actual = url2uri(non_url)
        expected = non_url
        self.assertEqual(actual, expected)

    def test_unicode_non_url_untouched(self):
        """Usually your local system allows unicode path"""
        unicode_non_url = 'ホーム/名前/dir'
        actual = url2uri(unicode_non_url)
        expected = unicode_non_url
        self.assertEqual(actual, expected)
