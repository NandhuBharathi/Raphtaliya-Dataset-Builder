import json
from pathlib import Path


class DatasetSaver:

    def __init__(
        self,
        dataset,
        file_path,
    ):

        self.dataset = dataset
        self.file_path = Path(file_path)


    def save(
        self,
        output_dir="processed"
    ):

        try:

            output_dir = Path(output_dir)

            output_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            # ----------------------------------
            # Dataset File
            # ----------------------------------

            dataset_name = (
                self.file_path.stem + ".json"
            )

            dataset_file = (
                output_dir / dataset_name
            )

            with open(
                dataset_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(

                    self.dataset,

                    file,

                    indent=4,

                    ensure_ascii=False

                )


            print("=" * 60)
            print("Dataset Saved Successfully")
            print("=" * 60)
            print(f"Directory : {output_dir}")
            print(f"Dataset   : {dataset_name}")
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

    saver = DatasetSaver(

        dataset=dataset,

        file_path="sample.csv"

    )

    saver.save()