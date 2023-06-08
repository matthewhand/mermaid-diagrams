
### Usage

To use the Mermaid Diagram Generator, follow these steps:

1. Set up an AWS Lambda function using the provided Python script.
2. Configure the required AWS Systems Manager (SSM) parameters with appropriate values.
3. Ensure proper IAM permissions for the Lambda function to access the SSM parameters and Amazon S3.
4. Create an OpenAI API key and configure the associated SSM parameter.

#### AWS Systems Manager Parameters

The following SSM parameters should be configured with appropriate values:

- `/api/github`: GitHub Access Token
- `/mermaid-diagrams/github-repositories`: JSON list of GitHub repositories to generate diagrams for
- `/mermaid-diagrams/output-s3-bucket`: Amazon S3 bucket URL to upload the generated diagrams
- `/mermaid-diagrams/cloudformation-template-filenames`: JSON list of CloudFormation template file names
- `/mermaid-diagrams/openai-api-key`: OpenAI API Key
- `/mermaid-diagrams/openai-model`: OpenAI model to use (e.g., GPT-4)
- `/mermaid-diagrams/openai-token-size`: Token size for OpenAI model (e.g., 8k)

#### IAM Permissions

Ensure that the IAM role associated with the Lambda function has the necessary permissions to access the AWS Systems Manager parameters and the Amazon S3 bucket.
