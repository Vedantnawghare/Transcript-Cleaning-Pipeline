"""
Filler word removal module
Removes unnecessary speech fillers from transcripts
"""


class FillerRemover:

    def __init__(self):
        self.filler_words = {
            "umm",
            "um",
            "uh",
            "hmm",
            "ah",
            "like",
            "you know",
            "basically",
            "actually",
            "so"
        }


    def remove(self, text: str) -> str:
        """
        Remove filler words from transcript

        Args:
            text: Raw transcript

        Returns:
            Clean transcript
        """

        words = text.split()

        cleaned_words = []

        for word in words:
            if word.lower() not in self.filler_words:
                cleaned_words.append(word)

        return " ".join(cleaned_words)