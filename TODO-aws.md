# TODO-aws.md
This comprehensive TODO list provides detailed instructions for each step in configuring the AWS Lambda function, setting up SSM parameters, and implementing the Python script to generate Mermaid diagrams based on CloudFormation templates using OpenAI. Follow these instructions to create a functional Mermaid generation system on AWS Lambda.

- [ ] 1. Set up AWS Lambda function:
  - Ensure boto3 is functional.
  - Click on the "Create function" button.
  - Choose "Author from scratch" and enter a unique name for your Lambda function.
  - Select Python as the runtime environment (e.g., Python 3.8).
  - Under "Function code", choose "Upload a .zip file" and upload the zipped code package containing your Python script and dependencies.
  - Configure the memory, timeout, and concurrency settings as desired.
  - Grant the Lambda function permission to access AWS Systems Manager and Amazon S3 by creating or attaching an IAM role with the necessary policies.
  - Click "Create function" to complete the setup.

- [ ] 2. Configure SSM parameters in AWS Systems Manager:
  - In the AWS Management Console, navigate to the AWS Systems Manager service.
  - Click on "Parameter Store" in the left sidebar.
  - Create the following SSM parameters, making sure to choose the "SecureString" type for sensitive information like the GitHub Access Token:
    - `/api/github`: GitHub Access Token
    - `/mermaid-diagrams/github-repositories`: JSON list of GitHub repositories to generate diagrams for
    - `/mermaid-diagrams/output-s3-bucket`: Amazon S3 bucket URL to upload the generated diagrams
    - `/mermaid-diagrams/cloudformation-template-filenames`: JSON list of CloudFormation template file names
    - `/mermaid-diagrams/openai-api-key`: OpenAI API Key
    - `/mermaid-diagrams/openai-model`: OpenAI model to use (e.g., GPT-4)
    - `/mermaid-diagrams/openai-token-size`: Token size for OpenAI model (e.g., 8k)
  - Make note of the parameter names and values, as these will be used in the Lambda function.

- [ ] 3. Modify the Python script to fetch SSM parameters:
  - Import the Boto3 library in your Python script to interact with AWS services.
  - Write a function that uses the Boto3 client for AWS Systems Manager to retrieve the values of the SSM parameters.
  - Call the function in your script to fetch the SSM parameter values and use them as needed in your code.

- [ ] 4. Set up OpenAI Python client:
  - Install the `openai` Python package using `pip install openai`.
  - Import the `openai` library in your Python script.
  - Configure the OpenAI client with your OpenAI API key obtained from the SSM parameter.

- [ ] 5. Modify the Python script to process CloudFormation templates and generate prompts for OpenAI:
  - Write a function to parse the JSON list of GitHub repositories obtained from the SSM parameter `/mermaid-diagrams/github-repositories`.
  - For each repository in the list, use the GitHub API to obtain the repository content and retrieve CloudFormation templates matching the file names specified in the SSM parameter.
  - Prepare a list of possible icons from the GitHub image repository.
  - Generate prompts for OpenAI using the contents of the CloudFormation templates and the list of possible icons.

- [ ] 6. Modify the Python script to generate Mermaid diagrams using OpenAI:
  - Write a function to call the OpenAI API with the generated prompts, the desired model (e.g., GPT-4), and token size (e.g., 8k) obtained from the SSM parameters.
  - Parse the API response to retrieve the generated Mermaid diagram syntax.
  - Save the Mermaid diagram syntax in memory or temporarily in the Lambda function's environment.

- [ ] 7. Modify the Python script to upload diagrams to an Amazon S3 bucket:
  - Write a function that uses the Boto3 library to interact with the Amazon S3 service.
  - For each generated Mermaid diagram, convert the diagram syntax to an image format (e.g., PNG, SVG) using a suitable Python library or API.
  - Upload the generated images to the Amazon S3 bucket specified in the SSM parameter `/mermaid-diagrams/output-s3-bucket`.

- [ ] 8. Add error handling, logging, and monitoring to the Python script:
  - Wrap critical sections of the script in try-except blocks to catch exceptions and errors during execution.
  - Configure the Lambda function's retry settings, if needed.
  - Set up logging using the AWS CloudWatch service and the Python `logging` module for better monitoring and debugging of the Lambda function.

- [ ] 9. Test the Lambda function:
  - Create test events in the AWS Lambda console to simulate the function's expected behavior.
  - Verify that the generated Mermaid diagrams are uploaded to the Amazon S3 bucket and that the entire process works as intended.

- [ ] 10. Deploy updates to the Lambda function:
  - Package and upload the updated Python script and dependencies as a .zip file to your Lambda function.
  - Test the updated Lambda function using the AWS Lambda console or other methods like invoking the function through AWS SDKs or API Gateway.


## New Considerations
1. Consider using AWS Glue for ETL jobs.
2. Consider using AWS Athena for querying data in S3.
5. Consider using AWS QuickSight for data visualization.
