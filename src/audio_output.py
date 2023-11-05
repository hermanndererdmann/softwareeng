import gtts

class audio_out:
    def __init__(self):
        pass

    def texttospeach(self, imgdata):
        gtts.text_to_speech('Hello, world! This is a test.')
        