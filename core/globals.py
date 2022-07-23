""" App global variables """

from handlers.TextHandler import (TextHandler,
                                  PDFTextHandler,
                                  DOCXTextHandler,
                                  RTFTextHandler)


# region GlobalVariables
AVAILABLE_HANDLERS = {
    '.pdf': PDFTextHandler,
    '.txt': TextHandler,
    '.rtf': RTFTextHandler,
    '.docx': DOCXTextHandler
}

ERRORS = []
# endregion
