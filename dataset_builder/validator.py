
import pandas as pd


class DatasetValidator:

    def __init__(self, dataset):

        self.dataset = dataset

    def validate(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Dataset Validation Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return False

            warnings = []

            # DataFrame
            if isinstance(self.dataset, pd.DataFrame):

                if self.dataset.empty:
                    warnings.append("Dataset is empty.")

                if self.dataset.duplicated().sum() > 0:
                    warnings.append(
                        f"Duplicate rows : {self.dataset.duplicated().sum()}"
                    )

                missing = (
                    self.dataset
                    .isnull()
                    .sum()
                    .sum()
                )

                if missing > 0:
                    warnings.append(
                        f"Missing values : {missing}"
                    )

            # List
            elif isinstance(self.dataset, list):

                if len(self.dataset) == 0:
                    warnings.append("List is empty.")

            # Dictionary
            elif isinstance(self.dataset, dict):

                if len(self.dataset) == 0:
                    warnings.append("Dictionary is empty.")

            # Text
            elif isinstance(self.dataset, str):

                if len(self.dataset.strip()) == 0:
                    warnings.append("Text is empty.")

            print("=" * 60)
            print("Dataset Validation")
            print("=" * 60)

            if warnings:

                print("Status : WARNING")

                for warning in warnings:

                    print(f"- {warning}")

            else:

                print("Status : PASSED")

            print("=" * 60)

            return len(warnings) == 0

        except Exception as error:

            print("=" * 60)
            print("Dataset Validation Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return False


if __name__ == "__main__":

    dataframe = pd.DataFrame({
        "id": [1, 2, 3],
        "name": [
            "Raphtaliya",
            "Dataset Builder",
            "Mark-1"
        ]
    })

    validator = DatasetValidator(dataframe)

    validator.validate()
