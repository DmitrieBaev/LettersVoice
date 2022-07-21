""" Handling text and preparing it for speech """

import pdfplumber  # PDF lib.


class LiveTextHandler:
    pass


class DocumentTextHandlerInterface:
    def __init__(self, path: str):
        """Simple Interface for handling file to str converting.

        :param path: [String] Path to file.
        """
        self.path2file = path

    def convert(self) -> str:
        """Converter method.

        :return: [String]
        """
        pass


class TextHandler(DocumentTextHandlerInterface):
    def __init__(self, path: str):
        """TXT Handler. Receiving path to file and converting data from file to string.

        :param path: [String] Path to file.
        """
        super().__init__(path)

    def convert(self) -> str:
        with open(file=self.path2file, mode='r') as txt:
            return txt.read()\
                      .replace('\n', '')  # Required to remove a pause in line breaks for speech.


class PDFTextHandler(DocumentTextHandlerInterface):
    def __init__(self, path: str):
        """PDF Handler. Receiving path to file and converting data from file to string.

        :param path: [String] Path to file.
        """
        super().__init__(path)

    def convert(self) -> str:
        with pdfplumber.PDF(open(file=self.path2file, mode='rb')) as pdf:
            return ''.join(
                # Represent pages as solid text.
                [page.extract_page() for page in pdf.pages]
            ).replace('\n', '')  # Required to remove a pause in line breaks for speech.


# TODO: Add DOC & DOCX Handler for 'en' and 'ru' languages
# class DOCTextHandler(DocumentTextHandlerInterface):
#     def __init__(self, path: str):
#         super().__init__(path)
#
#     def convert(self) -> str:
#         pass


# TODO: Add DJVU Handler for 'en' and 'ru' languages
# class DJVUTextHandler(DocumentTextHandlerInterface):
#     def __init__(self, path: str):
#         super().__init__(path)
#
#     def convert(self) -> str:
#         pass
