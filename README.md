# README.md

## Mermaid Diagram Generator for CloudFormation Templates

This AWS Lambda-based application automatically generates Mermaid diagrams based on the contents of CloudFormation templates in your GitHub repositories. The generated diagrams are uploaded to a specified Amazon S3 bucket.

Key features include:

- Processing multiple GitHub repositories and CloudFormation templates
- Generating Mermaid diagrams using OpenAI with a GPT-4 and 8k token size
- Uploading generated diagrams to an Amazon S3 bucket

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
