
from pathlib import Path
import pandas as pd


class CSVReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            dataframe = pd.read_csv(
                self.file_path,
                encoding="utf-8"
            )

            print("=" * 60)
            print("CSV File Read Successfully")
            print("=" * 60)
            print(f"File    : {self.file_path}")
            print(f"Rows    : {len(dataframe)}")
            print(f"Columns : {len(dataframe.columns)}")
            print("=" * 60)

            return dataframe

        except Exception as error:

            print("=" * 60)
            print("CSV File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = CSVReader("sample.csv")

    dataframe = reader.read()

    if dataframe is not None:
        print(dataframe.head())
