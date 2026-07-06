
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

            elif self.schema == "dictionary":

                records = self._format_dictionary()

            elif self.schema == "translation":

                records = self._format_translation()
            elif self.schema == "chatml":

                records = self._format_chatml()

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

    # ==========================================================
    # QA
    # ==========================================================

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

    # ==========================================================
    # Alpaca
    # ==========================================================

    def _format_alpaca(self):

        records = []

        for _, row in self.dataset.iterrows():

            prompt = str(row["instruction"])

            if "input" in self.dataset.columns:

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

    # ==========================================================
    # Table
    # ==========================================================

    def _format_table(self):

        return self.dataset.to_dict(
            orient="records"
        )

    # ==========================================================
    # Document
    # ==========================================================

    def _format_document(self):

        if isinstance(self.dataset, str):

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

        records = []

        if "content" in self.dataset.columns:

            column = "content"

        elif "text" in self.dataset.columns:

            column = "text"

        else:

            raise ValueError(
                "Document dataset must contain 'content' or 'text' column."
            )

        for _, row in self.dataset.iterrows():

            records.append({

                "messages": [

                    {
                        "role": "document",
                        "content": str(row[column])
                    }

                ]

            })

        return records

    # ==========================================================
    # Dictionary
    # ==========================================================

    def _format_dictionary(self):

        return self.dataset.to_dict(
            orient="records"
        )

    # ==========================================================
    # Translation
    # ==========================================================

    def _format_translation(self):

        records = []

        source_column = self.dataset.columns[0]
        target_column = self.dataset.columns[1]

        for _, row in self.dataset.iterrows():

            records.append({

                "messages": [

                    {
                        "role": "user",
                        "content": str(row[source_column])
                    },

                    {
                        "role": "assistant",
                        "content": str(row[target_column])
                    }

                ]

            })

        return records
# ==========================================================
# ChatML
# ==========================================================

def _format_chatml(self):

    import ast

    records = []

    for _, row in self.dataset.iterrows():

        messages = row["messages"]

        if isinstance(messages, str):

            messages = ast.literal_eval(messages)

        records.append({

            "messages": messages

        })

    return records


if __name__ == "__main__":

    dataframe = pd.DataFrame({

        "text": [

            "Hello World",

            "Raphtaliya AI"

        ]

    })

    formatter = DatasetFormatter(
        dataframe,
        "document"
    )

    dataset = formatter.format()

    print(dataset)
