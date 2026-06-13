from app.cleaner import TranscriptCleaner


def test_transcript_cleaning():

    cleaner = TranscriptCleaner()

    text = "umm i worked on python and docker"

    result = cleaner.clean(text)

    assert result == "I worked on Python and Docker."



def test_duplicate_removal():

    cleaner = TranscriptCleaner()

    text = "I I worked on Python Python"

    result = cleaner.clean(text)

    assert result == "I worked on Python."