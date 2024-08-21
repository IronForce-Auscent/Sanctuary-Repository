import os

from flask import *
from jinja2 import exceptions

from .data import *
from .auth import *

app = Flask(
    __name__, 
    static_folder="../static", 
    template_folder="../templates"
)

@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search = request.form["query"]
        if search == "":
            return render_template("search.html", response=["empty search query"])
        query_response = parse_query(search.strip())
        response = {}
        for entry in query_response:
            name, description, status = entry
            response[name] = [description, status]
        return render_template("search.html", response=response if response else ["no results found", search])
    return render_template("search.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        staffid = request.form["staffid"]
        password = request.form["password"]
        response, results = check_login(staffid, password)
        if response:
            return render_template("login.html", response="success", message=results)
        else:
            return render_template("login.html", response="failure")
    return render_template("login.html")

@app.route("/query", methods=["GET"])
def query():
    if request.method == "GET":
        page = request.args.get("page")
        if page:
            if ".." in page or "%2F" in page or page.startswith("/"):
                return redirect("/")
            try:
                return render_template(page)
            except exceptions.TemplateNotFound as e:
                referrer = request.referrer
                return redirect(referrer)
    return redirect("/")
