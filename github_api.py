import requests

def get_github_stats(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    try:
        repos_data = response.json()
    except ValueError:
        # If response is not JSON
        repos_data = []

    # Check if repos_data is a list
    if isinstance(repos_data, list):
        total_stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)
        public_repos = len(repos_data)
    else:
        total_stars = 0
        public_repos = 0

    return {
        "username": username,
        "public_repos": public_repos,
        "stars": total_stars
    }
