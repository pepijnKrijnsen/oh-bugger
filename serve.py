import main
from bottle import *

@route("/")
def serveHome():
    return template("./web/app.tpl")

@route("/<filename>")
def serveFile(filename):
    return static_file(filename, root = "./web")


@post("/store_new")
def userSubmitsTicket():
    title = request.forms.get("Subject")
    body = request.forms.get("Ticket body")
    if title == "" or body == "":
        return template("app.tpl")
    form_data = {}
    form_data["title"] = title
    form_data["body"] = body
    main.presenter.newTicket(form_data)
    return template("app.tpl")

run(host = "localhost", port = 8080, debug = True)
