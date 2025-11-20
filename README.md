🛡️ SHE-GUARD
Autonomous Women’s Safety Intelligence Agent

SHE-GUARD is an AI-powered safety companion designed to analyze threats, detect emergency levels, record evidence, and capture user location in real-time.
Built using Python, SHE-GUARD is suitable for Kaggle LLM Agents Capstone Projects, research, safety applications, and GitHub portfolio.

🚀 Features
🔍 1. Risk Assessment Agent

Analyzes user text for danger keywords and returns a risk score.

🗺️ 2. Location Agent

Automatically detects user location using IP-based geolocation API (ip-api.com).

🚨 3. Emergency Level Agent

Decides emergency severity:

LOW

MEDIUM

HIGH

📁 4. Evidence Builder Agent (Your requirement)

Captures and stores:

Event logs

Timestamps

Location history

(Audio snapshots can be added later once PyAudio is installed)

Evidence is stored in /evidence/ folder.

🤖 5. Supervisor Agent

Orchestrates all agents and triggers emergency workflows.

🔄 6. Emergency Workflow

Completes processing and returns structured safety insights.

📂 Project Structure
SHE-GUARD/
│   main.py
│
├── agents/
│   ├── supervisor.py
│   ├── risk_agent.py
│   ├── location_agent.py
│   ├── emergency_agent.py
│   └── evidence_agent.py
│
├── workflows/
│   └── emergency_workflow.py
│
└── evidence/
    ├── event_log.txt
    └── location_history.txt

🧠 Architecture Diagram
 ┌──────────────────┐        ┌──────────────────┐
 │   Risk Agent      │        │ Location Agent    │
 └─────────┬────────┘        └──────────┬────────┘
           │                             │
           ▼                             ▼
 ┌──────────────────┐        ┌──────────────────┐
 │ Emergency Agent   │        │ Evidence Agent    │
 └─────────┬────────┘        └──────────┬────────┘
           │                             │
           └──────────────┬──────────────┘
                          ▼
                 ┌────────────────────┐
                 │  Supervisor Agent   │
                 └──────────┬─────────┘
                            ▼
                 ┌────────────────────┐
                 │ Emergency Workflow  │
                 └────────────────────┘

🔌 API Used
IP-Geolocation API

API: http://ip-api.com/json/

No API key required

Fast & reliable

Used to detect city, region, country, latitude, longitude


2. Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt, create it:

requests


(We can add PyAudio later after it starts working.)

▶️ Run the Application
python main.py


Example:

You: someone is following me


System Output:

Risk Score: 3
Location: Kochi, Kerala, India (Lat:xx, Lon:xx)
Emergency Level: HIGH
Status: Workflow completed successfully

📁 Evidence Collection (Important Feature)

Stored automatically inside /evidence/

1. Event Log
evidence/event_log.txt

2. Location History
evidence/location_history.txt


Each entry includes:

Timestamp

Text event

IP-based city/region/country

Latitude & longitude

🛠️ Technologies Used

Python 3.10

Requests library

ip-api geolocation service

Modular agent-based architecture

Fully text-based LLM-style processing

🧭 Future Enhancements

(for Kaggle / GitHub professionalism)

Audio evidence recording (PyAudio)

SMS emergency alerts

WhatsApp quick alert system

Real-time tracking

Web dashboard

Mobile app companion (Flutter)

📜 License

This project is open-source and free to use.

DONE ✅

Your README.md is ready for GitHub.
