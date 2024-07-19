from flask import *
import sqlite3

app = Flask(__name__)

def query_db(db_url, query, parameters): 
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search = request.form["query"]
        return render_template("search.html", response=search)
    return render_template("search.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")

if __name__ == '__main__':
    app.run(debug=True)