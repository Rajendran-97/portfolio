from flask import Flask, render_template
from leetcode_api import get_leetcode_stats
from codechef_api import get_codechef_stats

app = Flask(__name__)

@app.route("/")
def home():
    # Profile info
    profile = {
        "name": "Rajendran Subramaniam",
        "role": "Python Full Stack Developer | AI & ML Enthusiast",
        "skills": [
            {"category": "Frontend", "details": ["React", "JavaScript", "HTML", "CSS", "Bootstrap", "Tailwind"]},
            {"category": "Backend", "details": ["Python", "Flask", "Django"]},
            {"category": "Database/Tools", "details": ["SQLite", "VS Code"]},
            {"category": "AI/ML", "details": ["Machine Learning", "Random Forest", "Linear Regression", "KNN", "SVM"]}
        ],
        "contact": "rajendransubramaniam97@gmail.com",
        "phone": "+91 8344546047",
        "resume": "/static/RajendranSubramaniam.pdf"
    }

    # Fetch dynamic stats
    leetcode = get_leetcode_stats("RajendranSubramaniam")
    codechef = get_codechef_stats("rajendran_97")

    # Optional: Print to console for debugging
    print("LeetCode:", leetcode)
    print("CodeChef:", codechef)

    return render_template(
        "index.html",
        profile=profile,
        leetcode=leetcode,
        codechef=codechef
    )

if __name__ == "__main__":
    app.run(debug=True)
