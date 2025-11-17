class EvidenceAgent:

    def __init__(self):
        self.logs = []

    def record_event(self, text):
        print("[EvidenceAgent] Logged:", text)
        self.logs.append(text)
