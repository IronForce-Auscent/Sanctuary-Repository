from flask import *
import sqlite3
import re

app = Flask(__name__)

# Logical functions

def connect_db(db_url): 
    return sqlite3.connect(db_url)
    
    return sanitized_query

def parse_query(query: str):
    # Compiles a set of expressions to be matched to
    expressions = {
        "name": re.compile(r"name:([^\s]+)"),
        "status": re.compile(r"status:([^\s]+)")
    }
    matches = {"name": [], "status": []}
    for key, value in expressions.items():
        matches[key] = value.findall(query)
        query = value.sub("", query).strip() # Removes all matched elements from the original query

    connection = connect_db("projects.db")
    cursor = connection.cursor()
    sqlquery = "SELECT name, description, status FROM projects WHERE "
    params = []
    if matches["name"] or matches["status"]:
        if matches["name"]:
            sqlquery += "name LIKE ?"
            params.append("%" + matches["name"][0] + "%")
        if matches["status"]:
            if matches["name"]: query += " AND "
            sqlquery += "status = ?"
            params.append(matches["status"][0])
    else:
        sqlquery += " name LIKE ? OR description LIKE ?"
        params.extend(["%" + query + "%", "%" + query + "%"])
    sqlquery += " COLLATE NOCASE"
    cursor.execute(sqlquery, params)
    results = cursor.fetchall() 
    connection.close()
    return results

# Flask endpoints

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
        query_response = parse_query(search)
        response = {}
        for entry in query_response:
            name, description, status = entry
            response[name] = [description, status]
        return render_template("search.html", response=response)
    return render_template("search.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")

if __name__ == '__main__':
    app.run(debug=True)