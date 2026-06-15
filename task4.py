import re

class TranscriptCleaner:

    def __init__(self):
        self.filler_words = [
            "um", "umm", "uh", "ah",
            "like", "you know", "actually"
        ]

        self.tech_terms = {
            "python": "Python",
            "docker": "Docker",
            "api": "API",
            "flask": "Flask",
            "django": "Django",
            "sql": "SQL",
            "html": "HTML",
            "css": "CSS",
            "javascript": "JavaScript",
            "ai": "AI",
            "ml": "ML"
        }

    def remove_fillers(self, text):

        for word in self.filler_words:
            pattern = r'\b' + re.escape(word) + r'\b'
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)

        return text

    def normalize_spaces(self, text):
        return " ".join(text.split())

    def normalize_technical_terms(self, text):

        words = text.split()

        normalized = []

        for word in words:
            clean_word = word.lower()

            if clean_word in self.tech_terms:
                normalized.append(self.tech_terms[clean_word])
            else:
                normalized.append(word)

        return " ".join(normalized)

    def fix_sentence(self, text):

        if not text:
            return text

        text = text[0].upper() + text[1:]

        if not text.endswith("."):
            text += "."

        return text

    def clean_transcript(self, text):

        text = self.remove_fillers(text)

        text = self.normalize_spaces(text)

        text = self.normalize_technical_terms(text)

        text = self.fix_sentence(text)

        return text


# Example Usage

cleaner = TranscriptCleaner()

transcript = input("Enter transcript: ")

cleaned = cleaner.clean_transcript(transcript)

print("\nCleaned Transcript:")
print(cleaned)