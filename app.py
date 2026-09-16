from flask import Flask, render_template, request, jsonify
from chatbot import get_service_response
from database import create_database, save_lead
import re

app = Flask(__name__)

create_database()

# Stores the current conversation while the app is running
user_sessions = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip()
    session_id = data.get("session_id", "default")

    if not message:
        return jsonify({"response": "Please type a message."})

    if session_id not in user_sessions:
        user_sessions[session_id] = {
            "stage": "services",
            "name": "",
            "phone": "",
            "email": "",
            "requirement": "",
            "budget": ""
        }

    session = user_sessions[session_id]
    stage = session["stage"]

    # Normal service conversation
    if stage == "services":
        lower_message = message.lower()

        if lower_message in ["yes", "yes please", "interested", "get started",
                             "contact me", "talk to team", "start"]:
            session["stage"] = "name"

            return jsonify({
                "response": "Great! I'd be happy to help you get started. May I know your name?"
            })

        service_response = get_service_response(message)

        return jsonify({
            "response": service_response +
            "\n\nWould you like to discuss your requirement with our team? Please type Yes to continue."
        })

    # Collect name
    if stage == "name":
        if len(message) < 2:
            return jsonify({"response": "Please enter a valid name."})

        session["name"] = message
        session["stage"] = "phone"

        return jsonify({
            "response": f"Nice to meet you, {message}! Please enter your phone number."
        })

    # Collect phone
    if stage == "phone":
        phone = re.sub(r"\D", "", message)

        if len(phone) < 10 or len(phone) > 15:
            return jsonify({
                "response": "Please enter a valid phone number containing 10 to 15 digits."
            })

        session["phone"] = message
        session["stage"] = "email"

        return jsonify({
            "response": "Thank you. Please enter your email address."
        })

    # Collect email
    if stage == "email":
        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not re.match(email_pattern, message):
            return jsonify({
                "response": "Please enter a valid email address."
            })

        session["email"] = message
        session["stage"] = "requirement"

        return jsonify({
            "response": "What is your project requirement? Please describe it briefly."
        })

    # Collect requirement
    if stage == "requirement":
        if len(message) < 3:
            return jsonify({
                "response": "Please provide a little more information about your requirement."
            })

        session["requirement"] = message
        session["stage"] = "budget"

        return jsonify({
            "response": "Thank you. What is your approximate budget for this project?"
        })

    # Collect budget and save lead
    if stage == "budget":
        session["budget"] = message

        save_lead(
            session["name"],
            session["phone"],
            session["email"],
            session["requirement"],
            session["budget"]
        )

        name = session["name"]

        # Reset conversation after saving
        user_sessions[session_id] = {
            "stage": "services",
            "name": "",
            "phone": "",
            "email": "",
            "requirement": "",
            "budget": ""
        }

        return jsonify({
            "response":
                f"Thank you, {name}! Your details have been submitted successfully. "
                "Our team can now review your requirement and contact you."
        })

    return jsonify({
        "response": "How can I help you with PRISM's services?"
    })


if __name__ == "__main__":
    app.run(debug=True)