
from pathlib import Path
from bs4 import BeautifulSoup
import markdown


class MarkdownReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            with open(
                self.file_path,
                mode="r",
                encoding="utf-8"
            ) as file:

                markdown_text = file.read()

            html = markdown.markdown(markdown_text)

            soup = BeautifulSoup(
                html,
                "html.parser"
            )

            text = soup.get_text(
                separator="\n",
                strip=True
            )

            print("=" * 60)
            print("Markdown File Read Successfully")
            print("=" * 60)
            print(f"File : {self.file_path}")
            print("=" * 60)

            return text

        except Exception as error:

            print("=" * 60)
            print("Markdown File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = MarkdownReader("sample.md")

    content = reader.read()

    if content is not None:
        print(content)
