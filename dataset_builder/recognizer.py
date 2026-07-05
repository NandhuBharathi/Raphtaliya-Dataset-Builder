
import pandas as pd


class DatasetRecognizer:

    SCHEMAS = {

        "qa": {
            "question",
            "answer"
        },

        "alpaca": {
            "instruction",
            "input",
            "output"
        },

        "prompt_response": {
            "prompt",
            "response"
        },

        "chatml": {
            "messages"
        },

        "sharegpt": {
            "conversations"
        }

    }

    def __init__(self, dataset):

        self.dataset = dataset

    def detect(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Dataset Recognition Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            schema = self._recognize()

            print("=" * 60)
            print("Dataset Recognized")
            print("=" * 60)
            print(f"Schema : {schema}")
            print("=" * 60)

            return schema

        except Exception as error:

            print("=" * 60)
            print("Dataset Recognition Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None

    def _recognize(self):

        # DataFrame
        if isinstance(self.dataset, pd.DataFrame):

            keys = {
                column.lower()
                for column in self.dataset.columns
            }

            return self._match(
                keys,
                default="table"
            )

        # List
        elif isinstance(self.dataset, list):

            if len(self.dataset) == 0:

                return "empty_list"

            first = self.dataset[0]

            if isinstance(first, dict):

                keys = {
                    key.lower()
                    for key in first.keys()
                }

                return self._match(
                    keys,
                    default="list"
                )

            return "list"

        # Dictionary
        elif isinstance(self.dataset, dict):

            keys = {
                key.lower()
                for key in self.dataset.keys()
            }

            return self._match(
                keys,
                default="dictionary"
            )

        # Text
        elif isinstance(self.dataset, str):

            return "document"

        return "unknown"

    def _match(
        self,
        keys,
        default
    ):

        for schema, required_keys in self.SCHEMAS.items():

            if required_keys.issubset(keys):

                return schema

        return default


if __name__ == "__main__":

    dataframe = pd.DataFrame({

        "question": [
            "What is AI?"
        ],

        "answer": [
            "Artificial Intelligence"
        ]

    })

    recognizer = DatasetRecognizer(
        dataframe
    )

    recognizer.detect()
