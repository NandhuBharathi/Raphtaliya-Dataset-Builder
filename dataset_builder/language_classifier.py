
import re


class LanguageClassifier:

    def __init__(self, dataset):

        self.dataset = dataset

    def classify(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Language Classification Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            text = self._extract_text()

            languages = self._detect_languages(text)

            print("=" * 60)
            print("Language Classified")
            print("=" * 60)
            print(f"Languages : {languages}")
            print("=" * 60)

            return {

                "languages": languages

            }

        except Exception as error:

            print("=" * 60)
            print("Language Classification Failed")
            print("=" * 60)
            print(f"Error : {error}")
            print("=" * 60)

            return None

    def _extract_text(self):

        if isinstance(self.dataset, str):

            return self.dataset

        try:

            if hasattr(self.dataset, "columns"):

                if "content" in self.dataset.columns:

                    return " ".join(

                        self.dataset["content"]

                        .fillna("")

                        .astype(str)

                        .head(100)

                    )

                elif "text" in self.dataset.columns:

                    return " ".join(

                        self.dataset["text"]

                        .fillna("")

                        .astype(str)

                        .head(100)

                    )

            return str(self.dataset.head(100))

        except Exception:

            return str(self.dataset)

    def _detect_languages(self, text):

        languages = []

        tamil = re.findall(
            r"[\u0B80-\u0BFF]",
            text
        )

        english = re.findall(
            r"[A-Za-z]",
            text
        )

        if english:

            languages.append("english")

        if tamil:

            languages.append("tamil")

        if not languages:

            languages.append("unknown")

        return languages


if __name__ == "__main__":

    sample = """

    வணக்கம்

    Hello

    """

    classifier = LanguageClassifier(sample)

    result = classifier.classify()

    print(result)
