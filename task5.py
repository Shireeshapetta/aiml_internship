import os
from flask import Flask, request, jsonify, render_template
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")


@app.route("/")
def home():
    return "Email Service Integration Running"


@app.route("/send_email", methods=["POST"])
def send_email():

    data = request.get_json()

    recipient = data.get("recipient")
    candidate = data.get("candidate")

    html_content = render_template(
        "email_template.html",
        candidate=candidate
    )

    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=recipient,
        subject="Interview Notification",
        html_content=html_content
    )

    try:

        sg = SendGridAPIClient(SENDGRID_API_KEY)

        response = sg.send(message)

        return jsonify({
            "status": "sent",
            "provider": "SendGrid",
            "recipient": recipient,
            "message_id": response.headers.get("X-Message-Id")
        })

    except Exception as e:

        return jsonify({
            "status": "failed",
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)