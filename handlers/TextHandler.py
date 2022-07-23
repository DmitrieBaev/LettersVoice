""" Handling text and preparing it for speech """

from pathlib import Path


class LiveTextHandler:
    pass


# region FileHandlers
class DocumentTextHandlerInterface:
    """Simple Interface for handling file to str converting."""

    @classmethod
    async def convert(cls, _path: Path) -> str:
        """Converter method. Receiving path to file and converting data from file to string.

        :param _path: [Path] Path to the file.
        :return: [String]
        """
        pass


class TextHandler(DocumentTextHandlerInterface):
    """TXT Handler."""

    @classmethod
    async def convert(cls, path2file: Path) -> str:
        import aiofiles

        async with aiofiles.open(file=path2file, mode='r') as f:
            content = await f.read()

        return content.replace('\n', '')  # Required to remove a pause in line breaks for speech.


class PDFTextHandler(DocumentTextHandlerInterface):
    """PDF Handler."""

    @classmethod
    async def convert(cls, path2file: Path) -> str:
        import pdfplumber  # PDF lib.

        with pdfplumber.PDF(open(file=path2file, mode='rb')) as pdf:
            return ''.join(
                # Represent pages as solid text.
                [page.extract_text() for page in pdf.pages]
            ).replace('\n', '')  # Required to remove a pause in line breaks for speech.


class DOCXTextHandler(DocumentTextHandlerInterface):
    """DOCX Handler."""

    @classmethod
    async def convert(cls, path2file: Path) -> str:
        import docx2txt  # DOCX lib.

        return docx2txt.process(path2file)\
                       .replace('\n', '')  # Required to remove a pause in line breaks for speech.


class RTFTextHandler(DocumentTextHandlerInterface):
    """DOCX Handler."""

    @classmethod
    async def convert(cls, path2file: Path) -> str:
        import aiofiles
        from striprtf.striprtf import rtf_to_text  # RTF lib.

        async with aiofiles.open(file=path2file, mode='r') as f:
            content = await f.read()

        return rtf_to_text(content)\
            .replace('\n', '')  # Required to remove a pause in line breaks for speech.


# TODO: Add DJVU Handler for 'en' and 'ru' languages
# class DJVUTextHandler(DocumentTextHandlerInterface):
#     def __init__(self, path: str):
#         super().__init__(path)
#
#     def convert(self) -> str:
#         pass

#endregion