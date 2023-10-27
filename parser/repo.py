from POM import POM


class Repository:
    def __init__(self, repo) -> None:
        self.repo = repo
        self.pom = {}
        self.pom_files = []

    def fetch_all_pom_files(self, path, recursive=False):
        contents = self.repo.get_contents(path)
        for content in contents:
            if content.type == "dir":
                if recursive == False:
                    continue
                self.parse_all_pom_files(content.path)
            elif content.name.endswith("pom.xml"):
                self.pom_files.append(content)

    def parse_all_pom_files(self, path="", recursive=False) -> None:
        self.fetch_all_pom_files(path, recursive=recursive)

        for file in self.pom_files:
            pom_content = POM(file)
            pom_content.parse_depenencies()
            self.pom[pom_content.path] = {
                "download_url": pom_content.download_url,
                "dependencies": pom_content.dependencies,
            }
