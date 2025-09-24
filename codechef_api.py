import requests
from bs4 import BeautifulSoup

def get_codechef_stats(username):
    url = f"https://www.codechef.com/users/{username}"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()  # Raise error for bad HTTP status
    except requests.exceptions.RequestException as e:
        print(f"CodeChef fetch error: {e}")
        return {"error": "Unable to fetch CodeChef data"}

    try:
        soup = BeautifulSoup(r.text, "html.parser")

        rating_div = soup.find("div", class_="rating-number")
        stars_span = soup.find("span", class_="rating")
        rank_tags = soup.find_all("a", class_="rating-ranks")

        rating = rating_div.text.strip() if rating_div else "N/A"
        stars = stars_span.text.strip() if stars_span else "N/A"
        global_rank = rank_tags[0].text.strip() if rank_tags else "N/A"

        return {
            "username": username,
            "rating": rating,
            "stars": stars,
            "global_rank": global_rank,
        }

    except Exception as e:
        print(f"CodeChef parsing error: {e}")
        return {"error": "Unable to parse CodeChef data"}
