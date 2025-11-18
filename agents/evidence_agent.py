import os
from datetime import datetime

class EvidenceAgent:
    def __init__(self, location_agent):
        self.location_agent = location_agent

        # Ensure evidence folder exists
        os.makedirs("evidence", exist_ok=True)

        self.event_log_file = "evidence/event_log.txt"
        self.location_history_file = "evidence/location_history.txt"

    # Add event logs
    def record_event(self, text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.event_log_file, "a") as f:
            f.write(f"[{timestamp}] {text}\n")

        print(f"[EvidenceAgent] Event logged: {text}")

    # Add location history snapshot
    def record_location(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        location = self.location_agent.get_location()

        with open(self.location_history_file, "a") as f:
            f.write(f"[{timestamp}] {location}\n")

        print("[EvidenceAgent] Location saved to history.")

    # Combined method for workflow
    def store_all_evidence(self, message, risk_score):
        self.record_event(f"User message: {message}")
        self.record_event(f"Risk score: {risk_score}")
        self.record_location()
