import main
from bottle import *

@route("/")
def serveHome():
    return static_file("index.html", root = "./web")

@post("/store_new")
def userSubmitsTicket():
    title = request.forms.get("subj")
    body = request.forms.get("tictext")
    form_data = {}
    form_data["title"] = title
    form_data["body"] = body
    main.presenter.newTicket(form_data)

run(host = "localhost", port = 8080, debug = True)
