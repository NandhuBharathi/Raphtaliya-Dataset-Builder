
import pandas as pd


class DatasetFormatter:

    def __init__(self, dataset, schema):

        self.dataset = dataset
        self.schema = schema

    def format(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Dataset Formatting Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            if self.schema == "qa":

                records = self._format_qa()

            elif self.schema == "alpaca":

                records = self._format_alpaca()

            elif self.schema == "table":

                records = self._format_table()

            elif self.schema == "document":

                records = self._format_document()

            else:

                raise ValueError(
                    f"Unsupported Schema : {self.schema}"
                )

            print("=" * 60)
            print("Dataset Formatted Successfully")
            print("=" * 60)
            print(f"Records : {len(records)}")
            print("=" * 60)

            return records

        except Exception as error:

            print("=" * 60)
            print("Dataset Formatting Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None

    # ----------------------------
    # QA
    # ----------------------------

    def _format_qa(self):

        records = []

        for _, row in self.dataset.iterrows():

            records.append({

                "messages": [

                    {
                        "role": "user",
                        "content": str(row["question"])
                    },

                    {
                        "role": "assistant",
                        "content": str(row["answer"])
                    }

                ]

            })

        return records

    # ----------------------------
    # Alpaca
    # ----------------------------

    def _format_alpaca(self):

        records = []

        for _, row in self.dataset.iterrows():

            prompt = str(row["instruction"])

            if str(row["input"]).strip():

                prompt += "\n" + str(row["input"])

            records.append({

                "messages": [

                    {
                        "role": "user",
                        "content": prompt
                    },

                    {
                        "role": "assistant",
                        "content": str(row["output"])
                    }

                ]

            })

        return records

    # ----------------------------
    # Table
    # ----------------------------

    def _format_table(self):

        return self.dataset.to_dict(
            orient="records"
        )

    # ----------------------------
    # Document
    # ----------------------------

    def _format_document(self):

        return [

            {

                "messages": [

                    {
                        "role": "document",
                        "content": self.dataset
                    }

                ]

            }

        ]


if __name__ == "__main__":

    dataframe = pd.DataFrame({

        "question": [
            "What is AI?"
        ],

        "answer": [
            "Artificial Intelligence"
        ]

    })

    formatter = DatasetFormatter(
        dataframe,
        "qa"
    )

    dataset = formatter.format()

    print(dataset)
