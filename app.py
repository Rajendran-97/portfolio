from flask import Flask, render_template

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

    # ✅ Manual coding stats (update when needed)
    leetcode = {
        "username": "RajendranSubramaniam",
        "ranking": "500000+",
        "reputation": "0",
        "star_rating": "0.5",
        "problems_solved": 5
    }

    codechef = {
        "username": "rajendran_97",
        "rating": "1350",
        "stars": "★",
        "global_rank": "N/A"
    }

    return render_template(
        "index.html",
        profile=profile,
        leetcode=leetcode,
        codechef=codechef
    )

if __name__ == "__main__":
    app.run(debug=True)
