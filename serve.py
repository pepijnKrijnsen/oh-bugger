import main
from bottle import *

@route("/<filename>")
def serveHome(filename):
    return static_file(filename, root = "./web")

@post("/store_new")
def userSubmitsTicket():
    title = request.forms.get("Subject")
    body = request.forms.get("Ticket body")
    print(title)
    print(body)
    if title == "" or body == "":
        return static_file("app.html", root = "./web")
    form_data = {}
    form_data["title"] = title
    form_data["body"] = body
    main.presenter.newTicket(form_data)
    return static_file("app.html", root = "./web")

run(host = "localhost", port = 8080, debug = True)
