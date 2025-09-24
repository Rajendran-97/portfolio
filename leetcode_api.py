import requests

def get_leetcode_stats(username):
    url = "https://leetcode.com/graphql"
    query = {
        "query": """
        query getUserProfile($username: String!) {
            matchedUser(username: $username) {
                username
                profile {
                    ranking
                    reputation
                    starRating
                }
                submitStatsGlobal {
                    acSubmissionNum {
                        difficulty
                        count
                        submissions
                    }
                }
            }
        }
        """,
        "variables": {"username": username},
    }

    try:
        response = requests.post(url, json=query, timeout=10)
        response.raise_for_status()  # Raise error for HTTP errors
        data = response.json()

        # Check if matchedUser exists
        matched_user = data.get("data", {}).get("matchedUser")
        if matched_user:
            return matched_user
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"LeetCode fetch error: {e}")
        return None
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return None
