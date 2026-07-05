
from pathlib import Path
import pandas as pd


class ParquetReader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def read(self):

        try:

            dataframe = pd.read_parquet(
                self.file_path
            )

            print("=" * 60)
            print("Parquet File Read Successfully")
            print("=" * 60)
            print(f"File    : {self.file_path}")
            print(f"Rows    : {len(dataframe)}")
            print(f"Columns : {len(dataframe.columns)}")
            print("=" * 60)

            return dataframe

        except Exception as error:

            print("=" * 60)
            print("Parquet File Read Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    reader = ParquetReader("sample.parquet")

    dataframe = reader.read()

    if dataframe is not None:
        print(dataframe.head())
