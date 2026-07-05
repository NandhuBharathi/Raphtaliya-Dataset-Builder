
import kagglehub
from pathlib import Path


class KaggleSource:

    def __init__(self, dataset):

        self.dataset = dataset

    def load(self):

        path = kagglehub.dataset_download(
            self.dataset
        )

        return Path(path)
