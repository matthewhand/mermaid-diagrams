
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.network import APIGateway

with Diagram('AWS Serverless Architecture Diagram', show=False):
    dns = Route53('<AWS Route53 Example Name>')
    lb = ELB('<AWS ELB Example Name>')

    with Cluster('Serverless Compute'):
        svc_group = [Lambda('<AWS Lambda Function Name 1>'), Lambda('<AWS Lambda Function Name 2>')]

    dynamodb = Dynamodb('<AWS DynamoDB Table Name>')
    api_gateway = APIGateway('<AWS API Gateway Example Name>')

    dns >> lb >> svc_group
    svc_group >> dynamodb
    api_gateway >> lb
