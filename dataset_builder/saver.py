
from pathlib import Path
import json

import pandas as pd


class DatasetSaver:

    def __init__(self, dataset):

        self.dataset = dataset

    def save(self, output_path):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Dataset Save Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            output_path = Path(output_path)

            output_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            extension = output_path.suffix.lower()

            # JSON
            if extension == ".json":

                with open(
                    output_path,
                    "w",
                    encoding="utf-8"
                ) as file:

                    json.dump(
                        self.dataset,
                        file,
                        indent=4,
                        ensure_ascii=False
                    )

            # JSONL
            elif extension == ".jsonl":

                with open(
                    output_path,
                    "w",
                    encoding="utf-8"
                ) as file:

                    for record in self.dataset:

                        file.write(
                            json.dumps(
                                record,
                                ensure_ascii=False
                            )
                        )

                        file.write("\n")

            # CSV
            elif extension == ".csv":

                pd.DataFrame(
                    self.dataset
                ).to_csv(
                    output_path,
                    index=False,
                    encoding="utf-8"
                )

            # Parquet
            elif extension == ".parquet":

                pd.DataFrame(
                    self.dataset
                ).to_parquet(
                    output_path,
                    index=False
                )

            else:

                raise ValueError(
                    f"Unsupported format : {extension}"
                )

            print("=" * 60)
            print("Dataset Saved Successfully")
            print("=" * 60)
            print(f"Path : {output_path}")
            print("=" * 60)

            return output_path

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
            "id": 1,
            "text": "Raphtaliya"
        },

        {
            "id": 2,
            "text": "Dataset Builder"
        }

    ]

    saver = DatasetSaver(dataset)

    saver.save("processed/sample.json")
