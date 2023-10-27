from github import Github
import os
from dotenv import load_dotenv

load_dotenv()


class GitClass:
    def __init__(self):
        self.git = Github(os.getenv("GITHUB_TOKEN"))
