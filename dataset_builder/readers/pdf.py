
from pathlib import Path
from pypdf import PdfReader


class PDFReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            reader = PdfReader(self.file_path)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

            print("=" * 60)
            print("PDF File Read Successfully")
            print("=" * 60)
            print(f"File  : {self.file_path}")
            print(f"Pages : {len(reader.pages)}")
            print("=" * 60)

            return text

        except Exception as error:

            print("=" * 60)
            print("PDF File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = PDFReader("sample.pdf")

    content = reader.read()

    if content:
        print(content[:500])
