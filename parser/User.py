from GitClass import GitClass
from repo import Repository


class User(GitClass):
    def __init__(self) -> None:
        super().__init__()
        self.user = self.git.get_user()
        self.repos = []

    def fetch_all_repo(self):
        self.repos = self.user.get_repos()

        return self.repos

    def get_repo_from_name(self, repo_name):
        return self.git.get_repo(repo_name)

    def parse_all_repo(self):
        repos = []
        for repo in self.fetch_all_repo():
            repos.append(repo.full_name)
        return repos

    def get_repo_dependency(self, repo_name, recusrive=False):
        repository = Repository(self.get_repo_from_name(repo_name))
        repository.parse_all_pom_files(recursive=recusrive)
        return repository.pom
