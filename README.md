# README.md

## Mermaid Diagram Generator for CloudFormation Templates

This AWS Lambda-based application automatically generates Mermaid diagrams based on the contents of CloudFormation templates in your GitHub repositories. The generated diagrams are uploaded to a specified Amazon S3 bucket.

Key features include:

- Processing multiple GitHub repositories and CloudFormation templates
- Generating Mermaid diagrams using OpenAI with a GPT-4 and 8k token size
- Uploading generated diagrams to an Amazon S3 bucket

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

### How It Works

The Mermaid Diagram Generator performs the following steps:

1. Fetches the SSM parameters.
2. Parses the GitHub repositories and CloudFormation templates.
3. Generates prompts for OpenAI using the CloudFormation templates' content and a list of possible icons from the GitHub image repository.
4. Calls the OpenAI API with the generated prompts, model, and token size to generate Mermaid diagram syntax.
5. Converts the Mermaid diagram syntax to an image format (e.g., PNG, SVG).
6. Uploads the generated diagrams to the specified Amazon S3 bucket.

### Contributing

If you would like to contribute to this project or report issues, please open a GitHub issue or submit a pull request.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
