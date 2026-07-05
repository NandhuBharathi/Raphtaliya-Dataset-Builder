
import pandas as pd


class DatasetCleaner:

    def __init__(self, dataset):

        self.dataset = dataset

    def clean(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Dataset Cleaning Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            # DataFrame
            if isinstance(self.dataset, pd.DataFrame):

                cleaned = self.dataset.copy()

                # Remove duplicate rows
                cleaned = cleaned.drop_duplicates()

                # Remove completely empty rows
                cleaned = cleaned.dropna(how="all")

                # Remove completely empty columns
                cleaned = cleaned.dropna(
                    axis=1,
                    how="all"
                )

                # Strip whitespace from text columns
                for column in cleaned.select_dtypes(
                    include="object"
                ).columns:

                    cleaned[column] = (
                        cleaned[column]
                        .astype(str)
                        .str.strip()
                    )

            # Text
            elif isinstance(self.dataset, str):

                cleaned = self.dataset.strip()

            # List
            elif isinstance(self.dataset, list):

                cleaned = [
                    item
                    for item in self.dataset
                    if item
                ]

            # Dictionary
            elif isinstance(self.dataset, dict):

                cleaned = {
                    key: value
                    for key, value in self.dataset.items()
                    if value is not None
                }

            else:

                cleaned = self.dataset

            print("=" * 60)
            print("Dataset Cleaned Successfully")
            print("=" * 60)

            return cleaned

        except Exception as error:

            print("=" * 60)
            print("Dataset Cleaning Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    dataframe = pd.DataFrame({
        "id": [1, 2, 2],
        "name": [
            " Raphtaliya ",
            "Dataset Builder",
            "Dataset Builder"
        ]
    })

    cleaner = DatasetCleaner(dataframe)

    cleaned = cleaner.clean()

    print(cleaned)
