class EmergencyAgent:

    def check_emergency_level(self, risk_score):

        if risk_score >= 8:
            return "HIGH"
        elif risk_score >= 4:
            return "MEDIUM"
        else:
            return "LOW"
