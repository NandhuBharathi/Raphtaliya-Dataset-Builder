
from pathlib import Path
import pandas as pd


class DatasetInspector:

    def __init__(self, dataset):

        self.dataset = dataset

    def inspect(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Dataset Inspection Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            report = {}

            # Pandas DataFrame
            if isinstance(self.dataset, pd.DataFrame):

                report["type"] = "DataFrame"
                report["rows"] = len(self.dataset)
                report["columns"] = len(self.dataset.columns)

                report["column_names"] = list(
                    self.dataset.columns
                )

                report["data_types"] = {
                    column: str(dtype)
                    for column, dtype in self.dataset.dtypes.items()
                }

                report["missing_values"] = (
                    self.dataset
                    .isnull()
                    .sum()
                    .to_dict()
                )

            # Dictionary
            elif isinstance(self.dataset, dict):

                report["type"] = "Dictionary"
                report["keys"] = list(self.dataset.keys())

            # List
            elif isinstance(self.dataset, list):

                report["type"] = "List"
                report["records"] = len(self.dataset)

            # Text
            elif isinstance(self.dataset, str):

                report["type"] = "Text"
                report["characters"] = len(self.dataset)
                report["words"] = len(
                    self.dataset.split()
                )

            # Local File
            elif isinstance(self.dataset, Path):

                report["type"] = "File"
                report["path"] = str(self.dataset)
                report["size_bytes"] = (
                    self.dataset.stat().st_size
                )

            # Unknown
            else:

                report["type"] = type(
                    self.dataset
                ).__name__

            print("=" * 60)
            print("Dataset Inspection")
            print("=" * 60)

            for key, value in report.items():

                print(f"{key:<20}: {value}")

            print("=" * 60)

            return report

        except Exception as error:

            print("=" * 60)
            print("Dataset Inspection Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    import pandas as pd

    dataframe = pd.DataFrame({
        "id": [1, 2, 3],
        "name": [
            "Raphtaliya",
            "Dataset Builder",
            "Mark-1"
        ]
    })

    inspector = DatasetInspector(dataframe)

    inspector.inspect()
