# TODO-aws.md
This comprehensive TODO list provides detailed instructions for each step in configuring the AWS Lambda function, setting up SSM parameters, and implementing the Python script to generate Mermaid diagrams based on CloudFormation templates using OpenAI. Follow these instructions to create a functional Mermaid generation system on AWS Lambda.

- [ ] 1. Create CloudFormation templates for AWS resources:
  - Create a new directory in your GitHub repository called `cloudformation-templates/`
  - Use YAML or JSON to define the CloudFormation templates for the required AWS resources, including:
  
    - [ ] 1.1 AWS Lambda function:
      - Define the Lambda function resource, including:
        - Function name
        - Runtime environment (e.g., Python 3.8)
        - Handler
        - Code source (e.g., S3 URI)
        - Required IAM role
        - Timeout and memory settings
    
    - [ ] 1.2 IAM roles and policies:
      - Define IAM roles and policies for the Lambda function, with permissions for:
        - Accessing AWS Systems Manager
        - Accessing Amazon S3
        - Executing Step Functions
      - Define IAM roles and policies for the API Gateway, allowing it to invoke the Lambda function.
      
    - [ ] 1.3 API Gateway:
      - Define the API Gateway resource, including:
        - API name
        - Endpoint type
      - Define resources and methods for the API
      - Set up the integration of the Lambda function with Lambda Proxy integration enabled
      
    - [ ] 1.4 SSM Parameters:
      - Define the SSM Parameters necessary for the Lambda function, including:
        - `/api/github`: GitHub Access Token
        - `/mermaid-diagrams/github-repositories`: JSON list of GitHub repositories to generate diagrams for
        - `/mermaid-diagrams/output-s3-bucket`: Amazon S3 bucket URL to upload the generated diagrams
        - `/mermaid-diagrams/cloudformation-template-filenames`: JSON list of CloudFormation template file names
        - `/mermaid-diagrams/openai-api-key`: OpenAI API Key
        - `/mermaid-diagrams/openai-model`: OpenAI model to use (e.g., GPT-3)
        - `/mermaid-diagrams/openai-token-size`: Token size for OpenAI model (e.g., 8k)
      - Set the Type of sensitive information like the GitHub Access Token and OpenAI API Key as "SecureString"
      
  - Add the CloudFormation templates to the `cloudformation-templates/` directory.
  
- [ ] 2. Deploy AWS resources using CloudFormation templates:
  - Use Boto3 or the AWS CLI, run the `create-stack` or `update-stack` command, providing the CloudFormation templates as input.
  - Wait for the stack creation or update to complete.


... continued in TODO-aws2.md.
