from agents.risk_agent import RiskAgent
from agents.location_agent import LocationAgent
from agents.emergency_agent import EmergencyAgent
from agents.evidence_agent import EvidenceAgent
from workflows.emergency_workflow import EmergencyWorkflow


class SupervisorAgent:
    def __init__(self):
        self.risk_agent = RiskAgent()
        self.location_agent = LocationAgent()
        self.emergency_agent = EmergencyAgent()
        self.evidence_agent = EvidenceAgent()
        self.workflow = EmergencyWorkflow()

    def process_input(self, user_message, user_id="USER-01"):

        print("\n--- SHE-GUARD SYSTEM STARTED ---")

        # 1) Risk Analysis
        risk_score = self.risk_agent.analyze_risk(user_message)

        # 2) Get IP-based Location
        location = self.location_agent.get_location()

        # 3) Emergency Level
        emergency_level = self.emergency_agent.check_emergency_level(risk_score)

        # 4) Evidence Logging
        self.evidence_agent.record_event("User message: " + user_message)
        self.evidence_agent.record_event(f"Risk score: {risk_score}")

        # 5) Full workflow (5 arguments)
        return self.workflow.run_workflow(
            risk_score,
            location,
            emergency_level,
            user_message,
            user_id
        )
