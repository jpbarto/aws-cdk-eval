To start a project you must first bootstrap it:

cdk bootstrap aws://acct-no/region

This will create various roles and an S3 bucket so that CDK can work with the AWS account to deploy your apps.

The following is based on https://docs.aws.amazon.com/cdk/v2/guide/hello_world.html

cdk synth then generates the cloudformation and cdk deploy deploys it


Next step is the python workshop at https://cdkworkshop.com/30-python.html
