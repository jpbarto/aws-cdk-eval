from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
)
from constructs import Construct

class TestNetworkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "TestNetworkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        vpc = ec2.Vpc (self, "CDKVPC",
            cidr="172.16.0.0/20",
            enable_dns_hostnames = True,
            enable_dns_support = True,
            max_azs = 3,
            nat_gateways = 3,
            subnet_configuration = [
                { 'cidrMask': 24, 'name': 'public', 'subnetType': ec2.SubnetType.PUBLIC},
                { 'cidrMask': 24, 'name': 'private', 'subnetType': ec2.SubnetType.PRIVATE_WITH_NAT},
                { 'cidrMask': 24, 'name': 'isolated', 'subnetType': ec2.SubnetType.PRIVATE_ISOLATED},
                { 'cidrMask': 24, 'name': 'endpoints', 'subnetType': ec2.SubnetType.PRIVATE_ISOLATED}
                ]
        )
