import functions_framework
import urllib3
import json
import traceback
from flask import current_app, escape

# import os
# import flask
# from slack_bolt import App
# from slack_bolt.adapter.socket_mode import SocketModeHandler

slack_webhook: str = 'https://hooks.slack.com/services/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'


@functions_framework.http
def notify_to_slack(request):
    """
    This method accepts dynamic parameters, But as json format
    :param request: Most Likely a json as a string
                    request (flask.Request): The request object.
                    <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
                    slack webhook can be set through request parameters
    :return: success String as per need
    """

    message_payload = str(request.data)[1:]

    # Fix for Windows
    import platform
    os_name = platform.system()
    if os_name.lower() == 'windows':
        message_payload = message_payload.replace('"', '\\\"')
        print('os name is windows')

    print(message_payload)

    notify_slack(message_payload)

    return message_payload


# Send Slack notification based on the given message
def notify_slack(message):
    try:
        slack_message = str(message)
        print(slack_message)
        http = urllib3.PoolManager()
        response = http.request('POST',
                                slack_webhook,
                                body=json.dumps(slack_message),
                                headers={'Content-Type': 'application/json'},
                                retries=False)

        print("trying to Push to Slack...")
        print(response.status)
        print(message)
        if response.status != 200:
            print("Trying Alternate method")
            import os
            cmd = 'curl -X POST -H \"Content-type: application/json\" --data ' + '"{}"'.format(
                message[1:-1]) + " " + slack_webhook
            print(cmd)
            os.system(cmd)
        else:
            print("Message Sent to Slack...")
            print(f"Message sent to Slack : {message}")
    except ConnectionError as e:
        traceback.print_exc()
    return True


# To run the framework run the below command
# functions_framework --target=notify_to_slack
"""
Full command with variations
functions_framework --target=notify_to_slack --host=<The host on which the Functions Framework listens for requests> \
--port=<The port on which the Functions Framework listens for requests> \
--source=<file containing function. by default main.py>
"""
