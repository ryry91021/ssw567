import os
import requests
from dotenv import load_dotenv

def get_github_token():
    """Loads GitHub token from .env or environment variables."""
    load_dotenv()
    return os.getenv("GITHUB_TOKEN")

def get_repositories(user, headers):
    """Fetches repositories for a given GitHub user."""
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 403:
        raise Exception("Too many GitHub API calls. Wait a while.")
    elif response.status_code != 200:
        raise Exception(f"Failed to retrieve repositories. HTTP Status code: {response.status_code}")

    return response.json()

def get_commitCount(repo_full_name, headers):
    """Fetches commit count for a given repository."""
    url = f"https://api.github.com/repos/{repo_full_name}/commits"
    response = requests.get(url, headers=headers)

    if response.status_code == 409:
        return 0  # Empty repo
    elif response.status_code != 200:
        raise Exception(f"Failed to retrieve commits for {repo_full_name}. Status code: {response.status_code}")

    return len(response.json())

def main(user):
    """Main function to fetch repositories and commit counts."""
    #check for token
    GITHUB_TOKEN = get_github_token()
    HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

    repositories = get_repositories(user, HEADERS)
    
    repo_data = {}
    for repo in repositories:
        repo_name = repo['name']
        repo_full_name = repo['full_name']
        
        commit_count = get_commitCount(repo_full_name, HEADERS)
        repo_data[repo_name] = commit_count

    return repo_data

if __name__ == "__main__":
    user = input("Enter a GitHub username (leave blank for 'ryry91021'): ").strip()
    if not user:
        user = 'ryry91021'
    
    results = main(user)
    for repo, commits in results.items():
        print(f"Repo: {repo}, Number of commits: {commits}")
