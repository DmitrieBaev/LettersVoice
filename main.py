""" main """

from pathlib import Path


if __name__ == '__main__':
    path2file = Path(input('Path to file: '))

    if not path2file.is_file():
        pass

    if path2file.suffix() == '.pdf':
        # Work with pdfplumber
        pass

    if path2file.suffix() in ['.doc', '.docx']:
        pass

    path2file.stem
