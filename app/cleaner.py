from app.filler_remover import FillerRemover
from app.normalizer import TextNormalizer
from app.advanced_cleaner import AdvancedCleaner



class TranscriptCleaner:


    def __init__(self):

        self.filler_remover = FillerRemover()

        self.normalizer = TextNormalizer()

        self.advanced_cleaner = AdvancedCleaner()



    def clean(self, text):

        text = self.filler_remover.remove(text)

        text = self.advanced_cleaner.process(text)

        text = self.normalizer.normalize(text)

        return text