from flask import Flask, render_template
from leetcode_api import get_leetcode_stats
from codechef_api import get_codechef_stats
from github_api import get_github_stats

app = Flask(__name__)

@app.route("/")
def home():
    profile = {
        "name": "Rajendran Subramaniam",
        "role": "Python Full Stack Developer | AI & ML Enthusiast",
        "skills": ["Python", "Flask", "Django", "React", "SQL", "Machine Learning"],
        "contact": "rajendransubramaniam97@gmail.com",
        "phone": "8344546047",
        "resume": "/static/RajendranSubramaniam.pdf"
    }

    # ✅ Your usernames
    leetcode = get_leetcode_stats("RajendranSubramaniam")
    codechef = get_codechef_stats("rajendran_97")
    github = get_github_stats("Rajendran-97")

    print("LeetCode:", leetcode)
    print("CodeChef:", codechef)
    print("GitHub:", github)

    return render_template("index.html",
                           profile=profile,
                           leetcode=leetcode,
                           codechef=codechef,
                           github=github)

if __name__ == "__main__":
    app.run(debug=True)
