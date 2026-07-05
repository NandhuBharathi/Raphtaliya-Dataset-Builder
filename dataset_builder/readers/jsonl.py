
from pathlib import Path
import json


class JSONLReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            data = []

            with open(
                self.file_path,
                mode="r",
                encoding="utf-8"
            ) as file:

                for line in file:

                    line = line.strip()

                    if line:

                        data.append(
                            json.loads(line)
                        )

            print("=" * 60)
            print("JSONL File Read Successfully")
            print("=" * 60)
            print(f"File    : {self.file_path}")
            print(f"Records : {len(data)}")
            print("=" * 60)

            return data

        except Exception as error:

            print("=" * 60)
            print("JSONL File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = JSONLReader("sample.jsonl")

    content = reader.read()

    if content is not None:
        print(content)
