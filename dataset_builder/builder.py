
from dataset_builder.reader_factory import ReaderFactory
from dataset_builder.inspector import DatasetInspector
from dataset_builder.recognizer import DatasetRecognizer
from dataset_builder.language_classifier import LanguageClassifier
from dataset_builder.domain_classifier import DomainClassifier
from dataset_builder.formatter import DatasetFormatter
from dataset_builder.validator import DatasetValidator
from dataset_builder.saver import DatasetSaver


class DatasetBuilder:

    def __init__(
        self,
        file_path,
    ):

        self.file_path = file_path
        self.dataset_name = dataset_name
        self.source = source

    def build(self):

        try:

            # ==========================================================
            # Reader
            # ==========================================================

            factory = ReaderFactory(
                self.file_path
            )

            reader = factory.get_reader()

            dataset = reader.read()

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

            languages = language_classifier.classify()

            # ==========================================================
            # Domain Classifier
            # ==========================================================

            domain_classifier = DomainClassifier(
                dataset
            )

            domains = domain_classifier.classify()

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
 ==========================================================
            # Saver
            # ==========================================================

            saver = DatasetSaver(

                dataset=formatted_dataset,

                file_path=self.file_path,
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

    builder = DatasetBuilder(

        file_path="sample.csv"

    )

    result = builder.build()

    print(result)
