import os
from twilio.rest import Client
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# load environment variables
load_dotenv()

app = Flask(__name__)

# defining auth variables and fetching them from .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
whatsapp_number = os.getenv("WHATSAPP_NUMBER")

# adding the auth variables to client modular
client = Client(account_sid, auth_token)

@app.route("/send_whatsapp", methods = ["POST"])
def send_whatsapp():
    data = request.get_json()
    recepient = data.get("to")
    message = data.get("message")

    if not recepient or not message:
        return jsonify({"error":"Missing 'to' or 'message' parameter"}), 400
    else:
        try:
            client.messages.create(
                body = message, 
                from_ = 'whatsapp:+14155238886',
                to = f"whatsapp:{recepient}"
            )
            return jsonify({"status":"success", "messages":"whatsapp notification sent"})
        except Exception as e:
            return jsonify({"error":str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)