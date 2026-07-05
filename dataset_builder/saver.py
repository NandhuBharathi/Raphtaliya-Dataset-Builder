
import json
from pathlib import Path


class DatasetSaver:

    def __init__(
        self,
        dataset,
        metadata=None,
        statistics=None
    ):

        self.dataset = dataset
        self.metadata = metadata
        self.statistics = statistics

    def save(self, output_dir="processed"):

        try:

            output_dir = Path(output_dir)

            output_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            # ----------------------------
            # Train Dataset
            # ----------------------------

            train_file = output_dir / "train.json"

            with open(
                train_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(

                    self.dataset,

                    file,

                    indent=4,

                    ensure_ascii=False

                )

            # ----------------------------
            # Metadata
            # ----------------------------

            if self.metadata is not None:

                metadata_file = (
                    output_dir / "metadata.json"
                )

                with open(

                    metadata_file,

                    "w",

                    encoding="utf-8"

                ) as file:

                    json.dump(

                        self.metadata,

                        file,

                        indent=4,

                        ensure_ascii=False

                    )

            # ----------------------------
            # Statistics
            # ----------------------------

            if self.statistics is not None:

                statistics_file = (
                    output_dir / "statistics.json"
                )

                with open(

                    statistics_file,

                    "w",

                    encoding="utf-8"

                ) as file:

                    json.dump(

                        self.statistics,

                        file,

                        indent=4,

                        ensure_ascii=False

                    )

            print("=" * 60)
            print("Dataset Saved Successfully")
            print("=" * 60)
            print(f"Directory : {output_dir}")
            print("=" * 60)

            return output_dir

        except Exception as error:

            print("=" * 60)
            print("Dataset Save Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    dataset = [

        {

            "messages": [

                {

                    "role": "user",

                    "content": "Hello"

                },

                {

                    "role": "assistant",

                    "content": "வணக்கம்"

                }

            ]

        }

    ]

    metadata = {

        "schema": "conversation",

        "languages": [

            "english",

            "tamil"

        ],

        "domains": [

            "general"

        ]

    }

    statistics = {

        "records": 1

    }

    saver = DatasetSaver(

        dataset,

        metadata,

        statistics

    )

    saver.save()
