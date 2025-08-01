from flask import Flask, render_template
from graph_api import get_users
from risk_analysis import analyze_users

app = Flask(__name__)

@app.route("/")
def home():
    users = get_users()
    risks = analyze_users(users)
    return render_template("dashboard.html", risks=risks)

if __name__ == "__main__":
    app.run(debug=True)
