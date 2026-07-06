
import re


class DomainClassifier:

    def __init__(self, dataset):

        self.dataset = dataset

    def classify(self):

        try:

            if self.dataset is None:

                print("=" * 60)
                print("Domain Classification Failed")
                print("=" * 60)
                print("Dataset is None")
                print("=" * 60)

                return None

            text = self._extract_text().lower()

            domains = self._detect_domains(text)

            print("=" * 60)
            print("Domain Classified")
            print("=" * 60)
            print(f"Domains : {domains}")
            print("=" * 60)

            return {

                "domains": domains

            }

        except Exception as error:

            print("=" * 60)
            print("Domain Classification Failed")
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

    def _detect_domains(self, text):

        domains = []

        rules = {

            "programming": [

                "python",
                "java",
                "javascript",
                "cpp",
                "c++",
                "c#",
                "html",
                "css",
                "sql",
                "def ",
                "class ",
                "import ",
                "return"

            ],

            "mathematics": [

                "equation",
                "algebra",
                "calculus",
                "matrix",
                "geometry",
                "integral",
                "derivative"

            ],

            "science": [

                "physics",
                "chemistry",
                "biology",
                "atom",
                "cell"

            ],

            "medical": [

                "doctor",
                "patient",
                "medicine",
                "disease",
                "hospital"

            ],

            "history": [

                "king",
                "empire",
                "war",
                "dynasty"

            ]

        }

        for domain, keywords in rules.items():

            if any(
                keyword in text
                for keyword in keywords
            ):

                domains.append(domain)

        if not domains:

            domains.append("general")

        return domains


if __name__ == "__main__":

    sample = """

    def add(a, b):
        return a + b

    """

    classifier = DomainClassifier(
        sample
    )

    result = classifier.classify()

    print(result)
