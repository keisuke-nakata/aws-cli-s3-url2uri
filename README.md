# aws-cli-s3-url2uri

Make `aws s3` commands work with URL showed in AWS web console.  
```bash
aws_s3_url2uri ls "https://console.aws.amazon.com/s3/home?region=<your_region>#&bucket=mybucket&prefix=mydir/" --profile myprof
```
will be converted into  
```bash
aws s3 ls s3://mybucket/mydir/ --profile myprof
```

circleci check
