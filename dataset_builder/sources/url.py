
from pathlib import Path
from urllib.request import urlretrieve


class URLSource:

    def __init__(
        self,
        url,
        output_directory="downloads"
    ):

        self.url = url
        self.output_directory = Path(output_directory)

    def load(self):

        try:

            self.output_directory.mkdir(
                parents=True,
                exist_ok=True
            )

            file_name = self.url.rstrip("/").split("/")[-1]

            if not file_name:
                file_name = "downloaded_file"

            destination = self.output_directory / file_name

            if not destination.exists():

                urlretrieve(
                    self.url,
                    destination
                )

            print("=" * 60)
            print("URL Download Successful")
            print("=" * 60)
            print(f"URL  : {self.url}")
            print(f"Path : {destination}")
            print("=" * 60)

            return destination

        except Exception as error:

            print("=" * 60)
            print("URL Download Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    source = URLSource(
        url="https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
    )

    source.load()
