import boto3
from flask import Flask
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

app = Flask(__name__)


@app.route("/live")
def goLive():
    client = boto3.resource(
        "sqs",
        region_name="us-east-2",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    queue = client.get_queue_by_name(QueueName="livestreamBool")
    response = queue.send_message(MessageBody="goLive")
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return '<h2>We\'re going live!</h2>\n<a href="http://twitch.tv/ConstructionCam">Click Here</a> to watch.'
    else:
        return "SQS not being written."


if __name__ == "__main__":
    app.run()
