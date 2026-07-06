
from pathlib import Path


class ReaderFactory:

    def __init__(self, file_path):

        self.file_path = file_path

    def get_reader(self):

        extension = Path(
            self.file_path
        ).suffix.lower()

        # CSV
        if extension == ".csv":

            from dataset_builder.readers.csv import CSVReader

            return CSVReader(
                self.file_path
            )

        # JSON
        elif extension == ".json":

            from dataset_builder.readers.json import JSONReader

            return JSONReader(
                self.file_path
            )

        # JSONL
        elif extension == ".jsonl":

            from dataset_builder.readers.jsonl import JSONLReader

            return JSONLReader(
                self.file_path
            )

        # TXT
        elif extension == ".txt":

            from dataset_builder.readers.txt import TXTReader

            return TXTReader(
                self.file_path
            )

        # PDF
        elif extension == ".pdf":

            from dataset_builder.readers.pdf import PDFReader

            return PDFReader(
                self.file_path
            )

        # DOCX
        elif extension == ".docx":

            from dataset_builder.readers.docx import DOCXReader

            return DOCXReader(
                self.file_path
            )

        # XML
        elif extension == ".xml":

            from dataset_builder.readers.xml import XMLReader

            return XMLReader(
                self.file_path
            )

        # HTML
        elif extension == ".html":

            from dataset_builder.readers.html import HTMLReader

            return HTMLReader(
                self.file_path
            )

        # Markdown
        elif extension == ".md":

            from dataset_builder.readers.markdown import MarkdownReader

            return MarkdownReader(
                self.file_path
            )

        # Parquet
        elif extension == ".parquet":

            from dataset_builder.readers.parquet import ParquetReader

            return ParquetReader(
                self.file_path
            )

        # EPUB
        elif extension == ".epub":

            from dataset_builder.readers.epub import EPUBReader

            return EPUBReader(
                self.file_path
            )

        raise ValueError(
            f"Unsupported file type: {extension}"
        )
