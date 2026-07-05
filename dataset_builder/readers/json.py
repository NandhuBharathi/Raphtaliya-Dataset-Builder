
from pathlib import Path
import json


class JSONReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            with open(
                self.file_path,
                mode="r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            print("=" * 60)
            print("JSON File Read Successfully")
            print("=" * 60)
            print(f"File : {self.file_path}")
            print("=" * 60)

            return data

        except Exception as error:

            print("=" * 60)
            print("JSON File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = JSONReader("sample.json")

    content = reader.read()

    if content is not None:
        print(content)
