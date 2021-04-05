import logging
import http.client
from typing import Any
from typing import List
from typing import Optional

class GitClient:
    logger: logging.Logger = ...
    client: http.client.HTTPSConnection = ...
    def __init__(
        self, name: str, email: str, owner: str, repo: str, oauth: str
    ) -> None: ...
    def get_branch_sha(self, branch_name: str) -> Optional[str]: ...
    def create_branch(self, base_branch: str, new_branch: str) -> Optional[str]: ...
    def create_blob(self, file_contents: str) -> str: ...
    def create_blob_tree(
        self, branch_sha: str, file_name: str, blob_sha: str
    ) -> str: ...
    def create_commit(self, branch_sha: str, tree_sha: str) -> str: ...
    def update_reference(self, branch_name: str, commit_sha: str) -> dict: ...
    def create_pull_request(
        self, base_branch: str, head_branch: str, pr_title: str, pr_body: str
    ) -> Optional[int]: ...
    def recover_pull_request(self, head_branch: str) -> Optional[int]: ...
    def add_lables(self, number: int, labels: List[str]) -> None: ...
    def send_template(
        self,
        base_branch: str,
        new_branch: str,
        file_name: str,
        file_contents: str,
        **kwargs: Any
    ) -> bool: ...
