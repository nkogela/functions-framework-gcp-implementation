import functions_framework
import urllib3
import json
import traceback

# import os
# Import Bolt for Python (github.com/slackapi/bolt-python)
# from slack_bolt import App

slack_webhook: str = 'https://hooks.slack.com/services/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'
xapp_token: str = 'xapp-1-A03CQEQH06Q-3430158740130-518e3082f9a09cbc17ee8c421d5c8452ab51014deb51f5fced6a4090507a3e7d'


@functions_framework.http
def notify_to_slack(request):
    # Implementation of Slack API
    # webhook_url = 'https://hooks.slack.com/services/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'
    webhook_url = 'https://hooks.slack.com/services/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'
    # The message to be delivered to Slack API
    message_payload = """{
        "slack_info": {
            "enable": "False",
            "channel_name": "#paidmedia_notification",
            "pipeline": {
                "project": "tbd",
                "name": "maxmind pipeline",
                "message": "whatever message"
            }
        }
    }"""
    run_slack_notification(webhook_url, message_payload)
    return 'Success'


# Send Slack notification based on the given message
def run_slack_notification(webhook_url, message):
    try:
        slack_message = {'text': message}
        print(slack_message)
        http = urllib3.PoolManager()
        response = http.request('POST',
                                webhook_url,
                                body=json.dumps(slack_message),
                                headers={'Content-Type': 'application/json'},
                                retries=False)
        print(response)
        print(dir(response))
        print("trying to Push to Slack...")
        print(response.status)
        if response.status != 200:
            print("Trying Alternate method")
            import os
            cmd = 'curl -X POST -H \"Content-type: application/json\" --data \"{\\\"text\\\":\\\"Hello, World!\\\"}\"' + " " + webhook_url
            print(cmd)
            os.system(cmd)
        else:
            print("Message Sent to Slack...")
    except Exception as e:
        traceback.print_exc()
    return True

# To run the framework run the below command
# functions_framework --target=notify_to_slack
