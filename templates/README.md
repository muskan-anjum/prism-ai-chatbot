# PRISM Website AI Chatbot

A web-based chatbot developed for PRISM to provide information about company services and collect potential customer leads.

## Features

- Interactive chatbot interface
- Professional and responsive frontend UI
- Provides information about PRISM services
- Collects customer lead details
- Validates phone numbers and email addresses
- Stores leads in an SQLite database
- Supports structured conversation flow

## PRISM Services

The chatbot provides information about:

- Website Development
- Mobile App Development
- CRM / ERP
- Odoo
- AI Automation
- AI Chatbots
- Digital Marketing
- DevOps / Cloud
- Blockchain

## Lead Collection

At the end of the conversation, the chatbot collects:

1. Name
2. Phone Number
3. Email Address
4. Project Requirement
5. Budget

The collected information is securely stored in a local SQLite database.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- SQLite

## Project Structure

prism-ai-chatbot/
- app.py
- chatbot.py
- database.py
- templates/
  - index.html
- static/
  - style.css
  - script.js
- requirements.txt
- README.md
- .gitignore

## How to Run

1. Create and activate a Python virtual environment.
2. Install the required packages:

   pip install -r requirements.txt

3. Run the application:

   python app.py

4. Open the application in your browser:

   http://127.0.0.1:5000

## Lead Flow

Service Enquiry → Chatbot Response → Name → Phone → Email → Requirement → Budget → Database

## Security

The local database, virtual environment, environment files and other development files are excluded from GitHub using `.gitignore`.

## Purpose

This project demonstrates a service-based website chatbot with an interactive frontend, backend conversation handling, input validation and lead management.