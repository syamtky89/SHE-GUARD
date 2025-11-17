class RiskAgent:

    def analyze_risk(self, message):
        message = message.lower()

        danger_words = [
            "help", "attack", "follow", "stalking",
            "danger", "police", "emergency", "harass"
        ]

        risk = sum(word in message for word in danger_words)

        risk_score = min(risk * 3, 10)  # Score 0 - 10

        print(f"[RiskAgent] Risk Score: {risk_score}")
        return risk_score
