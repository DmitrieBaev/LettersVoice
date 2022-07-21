""" Speech handlers. Converters and Savers. """

from gtts import gTTS  # Speech lib.


class LiveSpeechHandler:
    """ """
    pass


class TextSpeechHandler:
    def __init__(self, lang: str = 'en'):
        """Base speech handler. Receiving text string and voicing with gTTS.

        :param lang: [String] Speech language. (Example) 'ru', 'en'.
        """
        self.language = lang

    def convert(self, text: str):
        """Converter method. Voicing received data

        :param text: [String] Text to be spoken.
        :return: Raw record of speech.
        """
        return gTTS(text=text, lang=self.language, slow=False)


class SpeechSaver:
    def __init__(self, path: str, extension: str = 'mp3'):
        """Save raw record of speech.

        :param path: Path to the folder where the mp3 will be saved.
        """
        self.save_path = path
        self.save_ext = extension

    def save(self, raw_speech):
        """

        :param raw_speech: Raw speech recording to be saved as mp3.
        """
        raw_speech.save(f'{self.save_path}.{self.save_ext}')
