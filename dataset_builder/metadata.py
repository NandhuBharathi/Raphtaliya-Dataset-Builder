
from datetime import datetime


class DatasetMetadata:

    def __init__(
        self,
        dataset_name,
        source,
        schema,
        languages,
        domains,
        file_name
    ):

        self.dataset_name = dataset_name
        self.source = source
        self.schema = schema
        self.languages = languages
        self.domains = domains
        self.file_name = file_name

    def generate(self):

        try:

            metadata = {

                "dataset_name": self.dataset_name,

                "source": self.source,

                "schema": self.schema,

                "languages": self.languages,

                "domains": self.domains,

                "created_at": datetime.now().isoformat(),

                "file_name": self.file_name

            }

            print("=" * 60)
            print("Dataset Metadata Generated")
            print("=" * 60)

            for key, value in metadata.items():

                print(f"{key:<20}: {value}")

            print("=" * 60)

            return metadata

        except Exception as error:

            print("=" * 60)
            print("Metadata Generation Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    metadata = DatasetMetadata(

        dataset_name="Raphtaliya Sample",

        source="Local",

        schema="qa",

        languages=["english"],

        domains=["programming"],

        file_name="sample.csv"

    )

    result = metadata.generate()

    print(result)
