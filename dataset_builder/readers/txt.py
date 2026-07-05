
from pathlib import Path


class TXTReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            with open(
                self.file_path,
                mode="r",
                encoding="utf-8"
            ) as file:

                text = file.read()

            print("=" * 60)
            print("TXT File Read Successfully")
            print("=" * 60)
            print(f"File : {self.file_path}")
            print("=" * 60)

            return text

        except Exception as error:

            print("=" * 60)
            print("TXT File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = TXTReader("README.md")

    content = reader.read()

    print(content[:500])
