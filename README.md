# aws-cli-s3-url2uri

Make `aws s3` commands work with URL showed in AWS web console.  
`aws_s3_url2uri ls "https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix=" --profile myprof`  
will be converted into  
`aws s3 ls s3://mybucket/ --profile myprof`.
