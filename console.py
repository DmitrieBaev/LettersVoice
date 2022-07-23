""" main """

from pathlib import Path
import asyncio

import handlers.TextHandler as hl
from handlers.SpeechHandler import TextSpeechHandler, SpeechSaver


async def get_handler(suffix: str):
    """Returns the desired handler corresponding to the file type or None.

    :param suffix: [String] File extension.
    :return: Document handler or None.
    """
    from core.globals import AVAILABLE_HANDLERS, ERRORS

    try:
        return AVAILABLE_HANDLERS[suffix]
    except KeyError as e:
        ERRORS.append(f'[X] Handler for {e} filetype is unavailable!')
        return None


async def try2convert(path2file: Path):
    handler = await get_handler(path2file.suffix)
    if handler is None:
        return

    print('Reading file..')
    raw_content = await handler().convert(path2file)
    # print(raw_content)
    # print('Voicing text..')
    # raw_speech = await TextSpeechHandler().convert(raw_content, language='ru')
    # # raw_speech = speecher.convert(raw_text)
    # # speech_saver = SpeechSaver(path2file.stem)
    # print('Saving speech..')
    # # await SpeechSaver().save(raw_speech, path2folder=path2file.stem)
    # # speech_saver.save(raw_speech)
    # print('Completed!')


if __name__ == '__main__':
    asyncio.run(
        try2convert(
            Path(r'/home/quotoms/Projects/LettersVoice/data/file_ru.rtdf'),
            # optHandler.RTFTextHandler
        )
    )
    # try2convert(
    #     Path(r'/home/quotoms/Projects/LettersVoice/data/file_ru.txt')
    # )
