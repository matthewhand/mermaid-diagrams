
import os
from github import Github
# First create a Github instance:
g = Github(os.getenv('GITHUB_TOKEN'))
# Then get the specific repository
repo = g.get_repo('matthewhand/mermaid-diagrams')
# Get the workflows
workflows = repo.get_workflows()
# Get the pylint workflow
pylint_workflow = [workflow for workflow in workflows if workflow.name == 'Pylint'][0]
# Get the runs of the pylint workflow
runs = pylint_workflow.get_runs()
# Get the failed runs
failed_runs = [run for run in runs if run.conclusion == 'failure']
# For each failed run, get the logs
for run in failed_runs:
    print(f'Run ID: {run.id}')
    for log in run.get_logs().get_lines():
        print(log)
