""" Speech handlers. Converters and Savers. """

from typing import NoReturn
from gtts import gTTS  # Speech lib.
from gtts.tts import gTTSError


class LiveSpeechHandler:
    pass


class TextSpeechHandler:
    """Base speech handler."""

    @classmethod
    async def convert(cls, content, language: str = 'en') -> gTTS:
        """Converter method. Receiving text string and voicing with gTTS.

        :param content: [String] Text to be spoken.
        :param language: [String] Speech language. (Example) 'ru', 'en'.
        :return: Raw record of speech.
        """
        return gTTS(text=content, lang=language, slow=False)


class SpeechSaver:
    @classmethod
    async def save(cls,
                   raw_speech,
                   path2folder: str,
                   extension: str = 'mp3'
                   ) -> NoReturn:
        """Save raw record of speech.

        :param raw_speech: Raw speech recording to be saved.
        :param path2folder: [String] Path to the directory where the file will be saved.
        :param extension: [String] Extension of the file. (Example) 'mp3', 'wav'
        """
        try:
            raw_speech.save(f'{path2folder}.{extension}')
        except gTTSError:
            raise Exception(f'[X] Couldn\'t save speech into {extension} file!')
