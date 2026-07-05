
import pandas as pd


class DatasetFormatter:

    def __init__(self, dataset):

        self.dataset = dataset

    def format(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Dataset Formatting Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            # DataFrame
            if isinstance(self.dataset, pd.DataFrame):

                formatted = (
                    self.dataset
                    .to_dict(
                        orient="records"
                    )
                )

            # Dictionary
            elif isinstance(self.dataset, dict):

                formatted = [self.dataset]

            # List
            elif isinstance(self.dataset, list):

                formatted = self.dataset

            # Text
            elif isinstance(self.dataset, str):

                formatted = [
                    {
                        "text": self.dataset
                    }
                ]

            else:

                formatted = [
                    {
                        "data": str(self.dataset)
                    }
                ]

            print("=" * 60)
            print("Dataset Formatted Successfully")
            print("=" * 60)
            print(f"Records : {len(formatted)}")
            print("=" * 60)

            return formatted

        except Exception as error:

            print("=" * 60)
            print("Dataset Formatting Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    dataframe = pd.DataFrame({
        "id": [1, 2],
        "name": [
            "Raphtaliya",
            "Dataset Builder"
        ]
    })

    formatter = DatasetFormatter(dataframe)

    formatted = formatter.format()

    print(formatted)
