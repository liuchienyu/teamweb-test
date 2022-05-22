from flask import Flask, redirect, render_template, url_for
from pymongo import MongoClient
import pymongo
app = Flask(__name__)
CONNECTION_STRING ="mongodb+srv://dandy40605:1234@cluster0.qqbqe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING,tls=True, tlsAllowInvalidCertificates=True,tz_aware=True )#tls=True, tlsAllowInvalidCertificates=True為解決無法連線問題


@app.route("/")
def homepage():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    db = client.webdata
    document_code_data = db.news
    code_results = document_code_data.find({'category':'公告'})
    code_results.sort("make_time",pymongo.DESCENDING)#按照時間降序排列
    code_results.limit(10)#限制數量
    return render_template("home.html",code_results=code_results)

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/activity")
def activity():
    return render_template("activity.html")

@app.route("/service")
def service():
    return render_template("404.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/administration")
def administration():
    return render_template("administration.html")

@app.route("/train")
def train():
    return render_template("train.html")

@app.route("/academic")
def academic():
    return render_template("academic.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/recruit")
def recruit():
    return render_template("recruit.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/introduction")
def introduction():
    return render_template("introduction.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/team_public")
def team_public():
    return render_template("team_public.html")



if __name__ == "__main__":
    app.run(debug=True)
