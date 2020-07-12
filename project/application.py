from flask import Flask, render_template, session, redirect, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from cs50 import SQL
from helpers import login_required, apology

app = Flask(__name__)

db = SQL("sqlite:///final.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

username=""

def user():

    global username
    return username

@app.route('/')
def home():

    username = user()

    return render_template("home.html", username=username)

@app.route('/login', methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":

        global username

        username = request.form.get("uname")

        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          username)

        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("psw")):
            return apology("invalid username/password", 403)

        return redirect('/')

    else:
        return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():

    session.clear()

    if request.method == "POST":

        if request.form.get("username") == "":
            return apology("must provide username", 403)

        else:
            print("username is", request.form.get("username"))

        if request.form.get("password") == "":
            return apology("must provide password", 403)

        else:
            print("password is", request.form.get("password"))

        if not request.form.get("password") == request.form.get("con"):
            return apology("passwords don't match", 403)

        username = request.form.get("username")
        password = request.form.get("password")
        phash = generate_password_hash(password)

        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          username)

        if len(rows) != 0:
            return apology("username taken", 403)
        else:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       username, phash)

        return redirect('/register_')

    else:
        return render_template("register.html")

@app.route('/registeruser')
def registerconfirm():

    return render_template("register2.html")

@app.route('/profile')
def profile():

    username = user()

    id_ = db.execute("SELECT id FROM users WHERE username = ?",
                      username)

    for ids in id_:
        uid = ids["id"]

    follower = db.execute("SELECT * FROM follow WHERE followed_id = ?",
                          uid)

    followings = db.execute("SELECT * FROM follow WHERE follower_id = ?",
                            uid)

    post = db.execute("SELECT * FROM posts WHERE poster_id = ?",
                      uid)

    followers = len(follower)
    following = len(followings)
    posts = len(post)

    return render_template("profile.html", username=username, followers=followers, following=following, posts=posts)


@app.route('/create', methods=["GET", "POST"])
def create():

    if request.method == "POST":

        title = request.form.get("title")
        content = request.form.get("content")

        username = user()

        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          username)

        for row in rows:
            uid = row["id"]

        print(uid)
        print(title)
        print(content)

        db.execute("INSERT INTO posts (poster_id, post_title, post_text) VALUES (?, ?, ?)",
                   uid, title, content)

        return redirect('/')

    else:
        return render_template('create.html')

@app.route('/review', methods=["GET", "POST"])
def review():

    if request.method == "POST":

        title = request.form.get("title")
        content = request.form.get("content")

        print(title)
        print(content)

        return redirect('/')

    else:
        return render_template('review.html')

@app.route('/settings', methods=["GET", "POST"])
def settings():

    return render_template('settings.html')

@app.route('/forgot')
def forgot():

    session.clear()

    return render_template("forgot.html")

app.route('/logout')
def logout():

    session.clear()

    return redirect('/')