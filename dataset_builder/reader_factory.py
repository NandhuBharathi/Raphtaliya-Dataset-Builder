
from pathlib import Path

from dataset_builder.readers.csv import CSVReader
from dataset_builder.readers.json import JSONReader
from dataset_builder.readers.jsonl import JSONLReader
from dataset_builder.readers.txt import TXTReader
from dataset_builder.readers.pdf import PDFReader
from dataset_builder.readers.docx import DOCXReader
from dataset_builder.readers.xml import XMLReader
from dataset_builder.readers.html import HTMLReader
from dataset_builder.readers.markdown import MarkdownReader
from dataset_builder.readers.parquet import ParquetReader
from dataset_builder.readers.epub import EPUBReader


class ReaderFactory:

    def __init__(self, file_path):

        self.file_path = file_path

    def get_reader(self):

        extension = (
            Path(self.file_path)
            .suffix
            .lower()
        )

        readers = {

            ".csv": CSVReader,
            ".json": JSONReader,
            ".jsonl": JSONLReader,
            ".txt": TXTReader,
            ".pdf": PDFReader,
            ".docx": DOCXReader,
            ".xml": XMLReader,
            ".html": HTMLReader,
            ".md": MarkdownReader,
            ".parquet": ParquetReader,
            ".epub": EPUBReader

        }

        reader = readers.get(extension)

        if reader is None:

            raise ValueError(
                f"Unsupported file type : {extension}"
            )

        return reader(self.file_path)
