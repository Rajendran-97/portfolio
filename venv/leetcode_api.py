import requests

def get_leetcode_stats(username):
    url = "https://leetcode.com/graphql"
    query = {
        "query": """query getUserProfile($username: String!) {
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
        }""",
        "variables": {"username": username},
    }
    response = requests.post(url, json=query)
    data = response.json()
    return data["data"]["matchedUser"]
