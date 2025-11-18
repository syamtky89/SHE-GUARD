class EmergencyAgent:
    def __init__(self):
        pass

    def get_emergency_level(self, risk_score):
        """
        Convert risk score → emergency severity
        """

        if risk_score >= 80:
            return "CRITICAL"
        elif risk_score >= 60:
            return "HIGH"
        elif risk_score >= 40:
            return "MEDIUM"
        else:
            return "LOW"
