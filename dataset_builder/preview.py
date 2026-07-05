
import pandas as pd


class DatasetPreview:

    def __init__(self, dataset):

        self.dataset = dataset

    def show(self, rows=5):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Dataset Preview Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            print("=" * 60)
            print("Dataset Preview")
            print("=" * 60)

            if isinstance(self.dataset, pd.DataFrame):

                preview = self.dataset.head(rows)

            elif isinstance(self.dataset, list):

                preview = self.dataset[:rows]

            elif isinstance(self.dataset, dict):

                preview = dict(
                    list(self.dataset.items())[:rows]
                )

            elif isinstance(self.dataset, str):

                preview = "\n".join(
                    self.dataset.splitlines()[:rows]
                )

            else:

                preview = self.dataset

            print(preview)

            print("=" * 60)

            return preview

        except Exception as error:

            print("=" * 60)
            print("Dataset Preview Failed")
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

    preview = DatasetPreview(dataframe)

    preview.show()
