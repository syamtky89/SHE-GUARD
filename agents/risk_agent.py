import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import re


class RiskAgent:

    def __init__(self):
        # High-risk keywords
        self.high_risk_words = [
            "help", "attack", "danger", "kill", "rape",
            "harass", "follow", "stalking", "kidnap",
            "bleeding", "scream", "emergency", "please save",
            "threat", "scared", "fear", "unsafe", "violence"
        ]

        # Medium-risk keywords
        self.medium_risk_words = [
            "argue", "fight", "strange man", "drunk people",
            "uncomfortable", "worried", "disturb", "shouting",
        ]

        # Low-risk keywords
        self.low_risk_words = [
            "alone", "night", "dark", "unknown place"
        ]

        self.vectorizer = TfidfVectorizer(stop_words="english")

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text

    def keyword_risk_score(self, text):
        score = 0

        for word in self.high_risk_words:
            if word in text:
                score += 40

        for word in self.medium_risk_words:
            if word in text:
                score += 20

        for word in self.low_risk_words:
            if word in text:
                score += 10

        return score

    def semantic_risk(self, text):
        # AI-like semantic danger detector using TF-IDF
        danger_sentences = [
            "I am in danger",
            "Someone is attacking me",
            "Please help me",
            "I feel unsafe",
            "Someone is following me",
            "I am scared"
        ]

        corpus = danger_sentences + [text]

        tfidf = self.vectorizer.fit_transform(corpus)
        similarity = (tfidf * tfidf.T).toarray()

        # Last row is user input similarity with danger sentences
        danger_similarity = similarity[-1][:-1].mean()

        return danger_similarity * 100  # scale

    def analyze_risk(self, user_message):
        cleaned = self.clean_text(user_message)

        keyword_score = self.keyword_risk_score(cleaned)
        semantic_score = self.semantic_risk(cleaned)

        final_score = min(keyword_score + semantic_score, 100)

        # Determine risk level label
        if final_score >= 80:
            level = "CRITICAL"
        elif final_score >= 60:
            level = "HIGH"
        elif final_score >= 40:
            level = "MEDIUM"
        else:
            level = "LOW"

        print(f"[RiskAgent] Score={final_score}, Level={level}")

        return {
            "score": final_score,
            "level": level
        }
