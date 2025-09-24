import requests

def get_github_stats(username):
    url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"
    
    user_data = requests.get(url).json()
    repos_data = requests.get(repos_url).json()

    total_repos = len(repos_data)
    total_stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)

    return {
        "username": username,
        "name": user_data.get("name"),
        "followers": user_data.get("followers"),
        "public_repos": total_repos,
        "stars": total_stars,
        "profile_url": user_data.get("html_url"),
    }
