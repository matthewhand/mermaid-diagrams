
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
