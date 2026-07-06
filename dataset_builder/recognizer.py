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

    DICTIONARY_KEYS = [
        {"word", "definition"},
        {"word", "meaning"},
        {"word", "gloss"},
        {"word", "senses"}
    ]

    DOCUMENT_KEYS = [
        {"text"},
        {"content"},
        {"document"},
        {"article"},
        {"body"}
    ]

    TRANSLATION_KEYS = [
        {"en", "ta"},
        {"english", "tamil"},
        {"source", "target"},
        {"src", "tgt"},
        {"input", "target"},
        {"translation", "target"}
    ]

    def __init__(self, dataset):

        self.dataset = dataset

    def classify(self):

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

        if isinstance(self.dataset, pd.DataFrame):

            keys = {
                column.lower().strip()
                for column in self.dataset.columns
            }

            return self._detect(keys, "table")

        elif isinstance(self.dataset, list):

            if len(self.dataset) == 0:
                return "empty_list"

            first = self.dataset[0]

            if isinstance(first, dict):

                keys = {
                    key.lower().strip()
                    for key in first.keys()
                }

                return self._detect(keys, "list")

            return "list"

        elif isinstance(self.dataset, dict):

            keys = {
                key.lower().strip()
                for key in self.dataset.keys()
            }

            return self._detect(keys, "dictionary")

        elif isinstance(self.dataset, str):

            return "document"

        return "unknown"

    def _detect(self, keys, default):

        schema = self._match(keys)

        if schema:
            return schema

        for required in self.DICTIONARY_KEYS:
            if required.issubset(keys):
                return "dictionary"

        for required in self.DOCUMENT_KEYS:
            if required.issubset(keys):
                return "document"

        for required in self.TRANSLATION_KEYS:
            if required.issubset(keys):
                return "translation"

        return default

    def _match(self, keys):

        for schema, required_keys in self.SCHEMAS.items():

            if required_keys.issubset(keys):
                return schema

        return None
