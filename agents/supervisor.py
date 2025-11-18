from agents.risk_agent import RiskAgent
from agents.location_agent import LocationAgent
from agents.emergency_agent import EmergencyAgent
from agents.evidence_agent import EvidenceAgent
from workflows.emergency_workflow import EmergencyWorkflow


class SupervisorAgent:

    def __init__(self):
        print("\n[SHE-GUARD] Initializing Agents...")

        self.risk_agent = RiskAgent()
        self.location_agent = LocationAgent()
        self.emergency_agent = EmergencyAgent()

        # IMPORTANT FIX BELOW
        self.evidence_agent = EvidenceAgent(self.location_agent)

        self.workflow = EmergencyWorkflow()

        # Save initial location
        self.evidence_agent.record_location()

    def process_input(self, user_message):
        print("\n--- SHE-GUARD SYSTEM STARTED ---")

        # Risk Analysis
        risk_data = self.risk_agent.analyze_risk(user_message)
        risk_score = risk_data["score"]
        risk_level = risk_data["level"]

        self.evidence_agent.record_event(f"User Message: {user_message}")
        self.evidence_agent.record_event(f"Risk Score: {risk_score}")
        self.evidence_agent.record_event(f"Risk Level: {risk_level}")

        # Location
        location = self.location_agent.get_location()
        self.evidence_agent.record_event(f"Location: {location}")

        # Emergency level
        emergency_level = self.emergency_agent.get_emergency_level(risk_score)

        # Workflow execution
        result = self.workflow.run_workflow(
            risk=risk_score,
            location=location,
            emergency_level=emergency_level,
            user_message=user_message,
            user_id="USER01"
        )

        self.evidence_agent.record_event(f"Workflow Output: {result}")

        return result
