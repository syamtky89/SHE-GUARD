def __init__(self):
    print("\n[SHE-GUARD] Initializing Agents...")

    self.risk_agent = RiskAgent()
    self.location_agent = LocationAgent()
    self.emergency_agent = EmergencyAgent()
    self.evidence_agent = EvidenceAgent(self.location_agent)   # ✅ FIXED
    self.workflow = EmergencyWorkflow()

    # Save initial location
    self.evidence_agent.record_location()
