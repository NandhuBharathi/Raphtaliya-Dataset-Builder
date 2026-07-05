
from pathlib import Path
from datetime import datetime


class DatasetMetadata:

    def __init__(
        self,
        dataset_name,
        source,
        file_path=None,
        language="unknown",
        version="1.0",
        description="",
        author="",
        license="",
        tags=None
    ):

        self.dataset_name = dataset_name
        self.source = source
        self.file_path = file_path
        self.language = language
        self.version = version
        self.description = description
        self.author = author
        self.license = license
        self.tags = tags or []

    def generate(self):

        try:

            metadata = {

                "dataset_name": self.dataset_name,
                "source": self.source,
                "language": self.language,
                "version": self.version,
                "description": self.description,
                "author": self.author,
                "license": self.license,
                "tags": self.tags,
                "created_at": datetime.now().isoformat()

            }

            if self.file_path is not None:

                path = Path(self.file_path)

                metadata["file_name"] = path.name
                metadata["file_extension"] = path.suffix

                if path.exists():

                    metadata["file_size_bytes"] = (
                        path.stat().st_size
                    )

            print("=" * 60)
            print("Dataset Metadata")
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

        dataset_name="Sample Dataset",
        source="Local",
        file_path="sample.csv",
        language="English",
        version="1.0",
        description="Demo dataset",
        author="Raphtaliya",
        license="MIT",
        tags=["demo", "csv"]

    )

    metadata.generate()
