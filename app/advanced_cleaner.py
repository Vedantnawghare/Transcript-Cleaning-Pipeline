import re


class AdvancedCleaner:


    def remove_duplicate_words(self, text):

        words = text.split()

        cleaned = []

        previous = None

        for word in words:

            if word.lower() != previous:
                cleaned.append(word)

            previous = word.lower()


        return " ".join(cleaned)



    def clean_spaces(self, text):

        return re.sub(
            r"\s+",
            " ",
            text
        ).strip()



    def remove_repeated_punctuation(self, text):

        text = re.sub(
            r"[.!?]+",
            ".",
            text
        )

        return text



    def process(self, text):

        text = self.remove_duplicate_words(text)

        text = self.clean_spaces(text)

        text = self.remove_repeated_punctuation(text)

        return text