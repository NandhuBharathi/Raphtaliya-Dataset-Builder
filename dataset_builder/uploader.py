
from pathlib import Path
import os

from huggingface_hub import HfApi


class DatasetUploader:

    def __init__(self, token=None):

        self.token = token or os.getenv("HF_TOKEN")

        if not self.token:

            raise ValueError(
                "HF_TOKEN not found. Set it as an environment variable or pass it to DatasetUploader()."
            )

        self.api = HfApi()

    def upload(
        self,
        dataset_name,
        folder_path="processed",
        private=False
    ):

        try:

            folder_path = Path(folder_path)

            if not folder_path.exists():

                raise FileNotFoundError(
                    f"Folder not found: {folder_path}"
                )

            username = self.api.whoami(
                token=self.token
            )["name"]

            repo_id = f"{username}/{dataset_name}"

            self.api.create_repo(

                repo_id=repo_id,

                repo_type="dataset",

                token=self.token,

                private=private,

                exist_ok=True

            )

            self.api.upload_folder(

                repo_id=repo_id,

                repo_type="dataset",

                folder_path=str(folder_path),

                token=self.token,

                commit_message="Upload processed dataset"

            )

            print("=" * 60)
            print("Dataset Uploaded Successfully")
            print("=" * 60)
            print(f"Repository : {repo_id}")
            print(f"Folder     : {folder_path}")
            print("=" * 60)

            return repo_id

        except Exception as error:

            print("=" * 60)
            print("Dataset Upload Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    uploader = DatasetUploader()

    uploader.upload(

        dataset_name="Raphtaliya-Dataset-Test",

        folder_path="processed",

        private=False

    )
