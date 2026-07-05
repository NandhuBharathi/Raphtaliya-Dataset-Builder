
from pathlib import Path
from docx import Document


class DOCXReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            document = Document(self.file_path)

            paragraphs = []

            for paragraph in document.paragraphs:

                text = paragraph.text.strip()

                if text:

                    paragraphs.append(text)

            content = "\n".join(paragraphs)

            print("=" * 60)
            print("DOCX File Read Successfully")
            print("=" * 60)
            print(f"File : {self.file_path}")
            print(f"Paragraphs : {len(paragraphs)}")
            print("=" * 60)

            return content

        except Exception as error:

            print("=" * 60)
            print("DOCX File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = DOCXReader("sample.docx")

    content = reader.read()

    if content is not None:
        print(content)
