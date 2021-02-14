## README
1. Create app.py python script in app/ dir
2. Create Dockerfile
3. Create entry.sh

```
export AWS_ACCESS_KEY_ID=[YOUR_AWSKEY]
export AWS_SECRET_ACCESS_KEY=[YOUR_AWSSECRET]
export AWS_SESSION_TOKEN=[YOUR_AWSSECRET]

sudo docker build . -t lambda/python:3.9-alpine3.12
sudo docker run -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN -p 9000:8080 lambda/python:3.9-alpine3.12

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```
## NOTES
* Deploy to AWS

export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_SESSION_TOKEN=
