# functions-framework-gcp-implementation
A working functions framework implementation in python for implementing Cloud Functions and Slack Bolt API in Google Cloud Platform Environment

This project integrates following functionalities and utilizes power of Google Cloud platform (GCP)
1. functions-framework (python)
2. Cloud Functions (http trigger)
3. Slack API implementation.


To initiate this project, python virtual Environment is recommended.

Workflow:
1. Create a Cloud Function with http trigger
2. Implement and test it locally (Functions-framework comes handy for this scenario)
3. Send Dynamic message to Slack Channel using Slack-Bolt API for python

Steps:
1. Create your virtual environment:
python3 -m venv .venv

2. Activate the Virtual Environment
source .venv/bin/activate 

3. Adding your app credentials
Before creating and starting the app, you'll need to copy over the credentials for your app. Copy the Bot User OAuth Access Token under the OAuth & Permissions sidebar (talked about in the installation section).
You'll just be using a local project in this guide, so you'll save your bot token as an environment variable. In the command line, you'll export your token as SLACK_BOT_TOKEN:

export SLACK_BOT_TOKEN=xoxb-your-token

5. In addition to the access token, you'll need a signing secret. Your app's signing secret verifies that incoming requests are coming from Slack. Navigate to the Basic Information page from your app management page. Under App Credentials, copy the value for Signing Secret.
export SLACK_SIGNING_SECRET=your-signing-secret

6. If you don't have slack_bolt, Use below command in the command prompt.
pip install slack_bolt

