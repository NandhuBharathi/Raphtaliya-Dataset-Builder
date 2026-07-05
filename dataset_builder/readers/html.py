
from pathlib import Path
from bs4 import BeautifulSoup


class HTMLReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            with open(
                self.file_path,
                mode="r",
                encoding="utf-8"
            ) as file:

                html = file.read()

            soup = BeautifulSoup(
                html,
                "html.parser"
            )

            # Remove unwanted tags
            for tag in soup(
                [
                    "script",
                    "style",
                    "noscript"
                ]
            ):
                tag.decompose()

            text = soup.get_text(
                separator="\n",
                strip=True
            )

            print("=" * 60)
            print("HTML File Read Successfully")
            print("=" * 60)
            print(f"File : {self.file_path}")
            print("=" * 60)

            return text

        except Exception as error:

            print("=" * 60)
            print("HTML File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = HTMLReader("sample.html")

    content = reader.read()

    if content is not None:
        print(content)
