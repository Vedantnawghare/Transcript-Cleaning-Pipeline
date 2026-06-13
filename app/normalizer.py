import json
from pathlib import Path


class TextNormalizer:

    def __init__(self):

        config_path = Path(
            "configs/technical_terms.json"
        )

        with open(config_path, "r") as file:
            self.technical_terms = json.load(file)



    def normalize_terms(self, text):

        words = text.split()

        corrected_words = []

        for word in words:

            clean_word = word.lower().strip(".,!?")

            if clean_word in self.technical_terms:
                corrected_words.append(
                    self.technical_terms[clean_word]
                )
            else:
                corrected_words.append(word)

        return " ".join(corrected_words)



    def capitalize_sentence(self, text):

        if not text:
            return text

        return text[0].upper() + text[1:]



    def add_punctuation(self, text):

        if not text.endswith("."):
            text += "."

        return text



    def normalize(self, text):

        text = self.normalize_terms(text)

        text = self.capitalize_sentence(text)

        text = self.add_punctuation(text)

        return text