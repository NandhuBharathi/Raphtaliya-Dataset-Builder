
from pathlib import Path
import subprocess


class GitHubSource:

    def __init__(
        self,
        repository_url,
        output_directory="github_datasets"
    ):

        self.repository_url = repository_url
        self.output_directory = Path(output_directory)

    def load(self):

        # Create output directory
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        # Repository name
        repository_name = self.repository_url.rstrip("/").split("/")[-1]

        # Remove .git if present
        if repository_name.endswith(".git"):
            repository_name = repository_name[:-4]

        destination = self.output_directory / repository_name

        # Clone only if not already downloaded
        if not destination.exists():

            subprocess.run(
                [
                    "git",
                    "clone",
                    self.repository_url,
                    str(destination)
                ],
                check=True
            )

        return destination


if __name__ == "__main__":

    source = GitHubSource(
        repository_url="https://github.com/NandhuBharathi/Raphtaliya-Dataset-Builder.git"
    )

    path = source.load()

    print("=" * 60)
    print("GitHub Repository")
    print("=" * 60)
    print(path)
    print("=" * 60)
