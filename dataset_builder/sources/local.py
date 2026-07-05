
from pathlib import Path


class LocalSource:

    def __init__(self, path):

        self.path = Path(path)

    def load(self):

        try:

            if not self.path.exists():

                raise FileNotFoundError(
                    f"{self.path} does not exist."
                )

            print("=" * 60)
            print("Local Source Loaded Successfully")
            print("=" * 60)
            print(f"Path : {self.path}")
            print("=" * 60)

            return self.path

        except Exception as error:

            print("=" * 60)
            print("Local Source Loading Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None


if __name__ == "__main__":

    source = LocalSource("README.md")

    source.load()
