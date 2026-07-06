
from pathlib import Path
import shutil

from huggingface_hub import HfApi
from kaggle_secrets import UserSecretsClient
from datetime import datetime

class DatasetUploader:

    def __init__(self):

        self.api = HfApi()

        secrets = UserSecretsClient()

        self.token = secrets.get_secret("HF_TOKEN")

    def upload(
        self,
        dataset_name,
        folder_path="processed",
        private=False
    ):

        try:

            folder = Path(folder_path)

            if not folder.exists():

                raise FileNotFoundError(
                    f"{folder_path} not found."
                )
            json_files = list(folder.glob("*.json"))

            if not json_files:

                print("=" * 60)
                print("No Dataset Found")
                print("=" * 60)
                print("Nothing to upload.")
                print("=" * 60)
                return None

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
            print("=" * 60)
            print("Repository Ready")
            print("=" * 60)
            print(f"Repository : {repo_id}")
            print("=" * 60)
            commit_message = (
               f"Dataset Upload - "
               f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)
            self.api.upload_folder(

                repo_id=repo_id,

                repo_type="dataset",

                folder_path=str(folder),

                token=self.token,

                commit_message=commit_message

            )
            for file in folder.glob("*"):

                if file.is_file():
                   file.unlink()
            print("=" * 60)
            print("Dataset Uploaded Successfully")
            print("=" * 60)
            print(f"Repository : {repo_id}")
            print(f"Folder     : {folder}")
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
        dataset_name="Raphtaliya-Training-Datasets"
    )
