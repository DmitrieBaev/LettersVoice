""" App global variables """
# base libs
import os
# project modules
from handlers.TextHandler import (TextHandler,
                                  PDFTextHandler,
                                  DOCXTextHandler,
                                  RTFTextHandler)


AVAILABLE_HANDLERS = {
    '.pdf': PDFTextHandler,
    '.txt': TextHandler,
    '.rtf': RTFTextHandler,
    '.docx': DOCXTextHandler
}

AVAILABLE_FILTERS = 'Portable Documents (*.pdf);;' \
                    'Text files (*.txt);;' \
                    'Rich Text Format (*.rtf);;' \
                    'Microsoft Word Documents (*.docx)'

# MUTED = False

# PATH_TO_FILE = f''
# PATH_TO_FOLDER = f''
