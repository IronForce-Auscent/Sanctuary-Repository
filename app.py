from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search = request.form["search"]
        return redirect(url_for("search", response=search))
    return render_template("search.html")

if __name__ == '__main__':
    app.run(debug=True)