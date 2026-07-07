
from dataset_builder.reader_factory import ReaderFactory
from dataset_builder.inspector import DatasetInspector
from dataset_builder.recognizer import DatasetRecognizer
from dataset_builder.language_classifier import LanguageClassifier
from dataset_builder.domain_classifier import DomainClassifier
from dataset_builder.formatter import DatasetFormatter
from dataset_builder.validator import DatasetValidator
from dataset_builder.saver import DatasetSaver
from datasets import Dataset, DatasetDict
import pandas as pd


class DatasetBuilder:

    def __init__(self, source):
        self.source = source

    def build(self):

        try:

            # ==========================================================
            # Reader
            # ==========================================================

            if isinstance(self.source, Dataset):
                dataset=self.source.to_pandas()
                print("="*60)
                print("Hugging Face Dataset Loaded Successfully")
                print("="*60)
                print(f"Rows    : {len(dataset)}")
                print(f"Columns : {len(dataset.columns)}")
                print("="*60)
            elif isinstance(self.source, DatasetDict):
                raise ValueError("Please pass a dataset split. Example: dataset['train']")
            elif isinstance(self.source, pd.DataFrame):
                dataset=self.source
                print("="*60)
                print("Pandas DataFrame Loaded Successfully")
                print("="*60)
                print(f"Rows    : {len(dataset)}")
                print(f"Columns : {len(dataset.columns)}")
                print("="*60)
            elif isinstance(self.source, str):
                factory=ReaderFactory(self.source)
                reader=factory.get_reader()
                dataset=reader.read()
            else:
                raise TypeError(f"Unsupported input type : {type(self.source).__name__}")

            # ==========================================================
            # Inspector
            # ==========================================================

            inspector = DatasetInspector(
                dataset
            )

            inspector.inspect()

            # ==========================================================
            # Schema Recognizer
            # ==========================================================

            recognizer = DatasetRecognizer(
                dataset
            )

            schema = recognizer.classify()

            # ==========================================================
            # Language Classifier
            # ==========================================================

            language_classifier = LanguageClassifier(
                dataset
            )

            language_classifier.classify()

            # ==========================================================
            # Domain Classifier
            # ==========================================================

            domain_classifier = DomainClassifier(
                dataset
            )

            domain_classifier.classify()

            # ==========================================================
            # Formatter
            # ==========================================================

            formatter = DatasetFormatter(
                dataset,
                schema
            )

            formatted_dataset = formatter.format()

            # ==========================================================
            # Validator
            # ==========================================================

            validator = DatasetValidator(
                formatted_dataset
            )

            valid = validator.validate()

            if not valid:

                print("=" * 60)
                print("Dataset Validation Failed")
                print("=" * 60)

                return None

            # ==========================================================
            # Saver
            # ==========================================================

            saver = DatasetSaver(

                dataset=formatted_dataset,

                file_path=self.source if isinstance(self.source, str) else "dataset",
            )

            output_path = saver.save()

            if output_path is None:

                return None

            print("=" * 60)
            print("Dataset Builder Completed Successfully")
            print("=" * 60)

            return {

                "dataset": formatted_dataset,



                "output": output_path

            }

        except Exception as error:

            print("=" * 60)
            print("Dataset Builder Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    builder = DatasetBuilder("sample.csv")

    result = builder.build()

    print(result)
