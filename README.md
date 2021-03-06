[![PyPI version](https://badge.fury.io/py/aws-s3-url2uri.svg)](https://badge.fury.io/py/aws-s3-url2uri)
[![Circle CI](https://circleci.com/gh/keisuke-nakata/aws-cli-s3-url2uri.svg?style=shield&circle-token=d6eef26322de7a44559b42d363878b08e0a20cbf)](https://circleci.com/gh/keisuke-nakata/aws-cli-s3-url2uri)

# aws-cli-s3-url2uri

Make `aws s3` commands work with URL showed in AWS web console.  
```bash
aws_s3_url2uri ls "https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix=mydir/" --profile myprof
```
will be converted into  
```bash
aws s3 ls s3://mybucket/mydir/ --profile myprof
```

# install
```bash
pip install aws-s3-url2uri
```  
and command `aws_s3_url2uri` will be available.
