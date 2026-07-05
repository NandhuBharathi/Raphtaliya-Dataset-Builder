
from datasets import load_dataset


class HuggingFaceSource:

    def __init__(
        self,
        dataset_name,
        dataset_config=None,
        dataset_split="train"
    ):

        self.dataset_name = dataset_name
        self.dataset_config = dataset_config
        self.dataset_split = dataset_split

    def load(self):

        dataset = load_dataset(
            path=self.dataset_name,
            name=self.dataset_config,
            split=self.dataset_split
        )

        return dataset
