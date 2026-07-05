
from pathlib import Path
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


class EPUBReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            book = epub.read_epub(self.file_path)

            text = []

            for item in book.get_items():

                if item.get_type() == ebooklib.ITEM_DOCUMENT:

                    soup = BeautifulSoup(
                        item.get_content(),
                        "html.parser"
                    )

                    content = soup.get_text(
                        separator="\n",
                        strip=True
                    )

                    if content:

                        text.append(content)

            content = "\n\n".join(text)

            print("=" * 60)
            print("EPUB File Read Successfully")
            print("=" * 60)
            print(f"File : {self.file_path}")
            print("=" * 60)

            return content

        except Exception as error:

            print("=" * 60)
            print("EPUB File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = EPUBReader("sample.epub")

    content = reader.read()

    if content is not None:
        print(content)
