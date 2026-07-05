
from pathlib import Path
import xml.etree.ElementTree as ET


class XMLReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            tree = ET.parse(self.file_path)

            root = tree.getroot()

            text = []

            for element in root.iter():

                if element.text:

                    value = element.text.strip()

                    if value:

                        text.append(value)

            content = "\n".join(text)

            print("=" * 60)
            print("XML File Read Successfully")
            print("=" * 60)
            print(f"File : {self.file_path}")
            print("=" * 60)

            return content

        except Exception as error:

            print("=" * 60)
            print("XML File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = XMLReader("sample.xml")

    content = reader.read()

    if content is not None:
        print(content)
