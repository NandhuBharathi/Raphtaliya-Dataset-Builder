
import pandas as pd


class DatasetStatistics:

    def __init__(self, dataset):

        self.dataset = dataset

    def generate(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Statistics Generation Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            report = {}

            if isinstance(self.dataset, pd.DataFrame):

                report["rows"] = len(self.dataset)
                report["columns"] = len(self.dataset.columns)

                report["numeric_columns"] = list(
                    self.dataset.select_dtypes(
                        include="number"
                    ).columns
                )

                report["text_columns"] = list(
                    self.dataset.select_dtypes(
                        include="object"
                    ).columns
                )

                report["missing_values"] = (
                    self.dataset
                    .isnull()
                    .sum()
                    .to_dict()
                )

                report["duplicate_rows"] = int(
                    self.dataset.duplicated().sum()
                )

            elif isinstance(self.dataset, str):

                report["characters"] = len(self.dataset)
                report["words"] = len(self.dataset.split())
                report["lines"] = len(self.dataset.splitlines())

            elif isinstance(self.dataset, list):

                report["records"] = len(self.dataset)

            elif isinstance(self.dataset, dict):

                report["keys"] = len(self.dataset.keys())

            else:

                report["type"] = type(self.dataset).__name__

            print("=" * 60)
            print("Dataset Statistics")
            print("=" * 60)

            for key, value in report.items():

                print(f"{key:<20}: {value}")

            print("=" * 60)

            return report

        except Exception as error:

            print("=" * 60)
            print("Statistics Generation Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    dataframe = pd.DataFrame({
        "id": [1, 2, 3],
        "name": [
            "Raphtaliya",
            "Dataset Builder",
            "Mark-1"
        ]
    })

    statistics = DatasetStatistics(dataframe)

    statistics.generate()
