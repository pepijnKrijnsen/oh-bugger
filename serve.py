import main
from bottle import *

@route("/<filename>")
def serveHome(filename):
    return static_file(filename, root = "./web")

@post("/store_new")
def userSubmitsTicket():
    title = request.forms.get("subj")
    body = request.forms.get("tictext")
    form_data = {}
    form_data["title"] = title
    form_data["body"] = body
    main.presenter.newTicket(form_data)

run(host = "localhost", port = 8080, debug = True)
