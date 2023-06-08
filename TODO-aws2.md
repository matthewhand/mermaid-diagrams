
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

... continued in TODO-aws3.md.
