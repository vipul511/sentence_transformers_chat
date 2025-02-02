import git
import os

def clone_github_repo(repo_url, local_path="repo"):
    """Clone a GitHub repository to a local folder."""
    if os.path.exists(local_path):
        print("Repo already cloned. Skipping...")
    else:
        git.Repo.clone_from(repo_url, local_path)
        print(f"✅ Cloned {repo_url} into {local_path}")

repo_url = "https://github.com/jennapederson/cloudformation-examples.git"
clone_github_repo(repo_url)

