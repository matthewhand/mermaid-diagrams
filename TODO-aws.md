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

- [ ] 3. Set up AWS Lambda function:
  - Ensure boto3 is functional.
  - Initialize a new project directory containing your Python script and dependencies.
  - Choose Python as the runtime environment (e.g., Python 3.8).
  - Reference your Lambda function in the respective CloudFormation template.
  - Deploy the Lambda function using AWS Serverless Application Model (SAM) or another deployment tool.
  - Use boto3 to execute the `create-stack` or `update-stack` command to launch or update the CloudFormation stack with the template that defines your AWS resources.

- [ ] 4. Modify the Python script to fetch SSM parameters:
  - Import the Boto3 library in your Python script to interact with AWS services.
  - Write a function that uses the Boto3 client for AWS Systems Manager to retrieve the values of the SSM parameters.
  - Call the function in your script to fetch the SSM parameter values and use them as needed in your code.

- [ ] 5. Set up OpenAI Python client:
  - Install the `openai` Python package using `pip install openai`.
  - Import the `openai` library in your Python script.
  - Configure the OpenAI client with your OpenAI API key obtained from the SSM parameter.

- [ ] 6. Modify the Python script to process CloudFormation templates and generate prompts for OpenAI:
  - Write a function to parse the JSON list of GitHub repositories obtained from the SSM parameter `/mermaid-diagrams/github-repositories`.
  - For each repository in the list, use the GitHub API to obtain the repository content and retrieve CloudFormation templates matching the file names specified in the SSM parameter.
  - Prepare a list of possible icons from the GitHub image repository.
  - Generate prompts for OpenAI using the contents of the CloudFormation templates and the list of possible icons.

- [ ] 7. Modify the Python script to generate Mermaid diagrams using OpenAI:
  - Write a function to call the OpenAI API with the generated prompts, the desired model (e.g., GPT-3), and token size (e.g., 8k) obtained from the SSM parameters.
  - Parse the API response to retrieve the generated Mermaid diagram syntax.
  - Save the Mermaid diagram syntax in memory or temporarily in the Lambda function's environment.

- [ ] 8. Modify the Python script to upload diagrams to an Amazon S3 bucket:
  - Write a function that uses the Boto3 library to interact with the Amazon S3 service.
  - For each generated Mermaid diagram, convert the diagram syntax to an image format (e.g., PNG, SVG) using a suitable Python library or API.
  - Upload the generated images to the Amazon S3 bucket specified in the SSM parameter `/mermaid-diagrams/output-s3-bucket`.

- [ ] 9. Implement GitHub webhook integration using CloudFormation template and Lambda function:
  - Update your Lambda function code to handle the GitHub webhook requests and start the AWS Step Functions state machine execution accordingly.
  - Use boto3 to create a new GitHub webhook with the "Payload URL" pointing to your API Gateway endpoint and specifying the "Label" event.

- [ ] 10. Add error handling, logging, and monitoring to the Python script:
  - Wrap critical sections of the script in try-except blocks to catch exceptions and errors during execution.
  - Configure the Lambda function's retry settings, if needed.
  - Set up logging using the AWS CloudWatch service and the Python `logging` module for better monitoring and debugging of the Lambda function.

- [ ] 11. Test the Lambda function:
  - Create test events in the AWS Lambda console to simulate the function's expected behavior.
  - Verify that the generated Mermaid diagrams are uploaded to the Amazon S3 bucket and that the entire process works as intended.
