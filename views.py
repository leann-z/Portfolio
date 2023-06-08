from flask import Blueprint, render_template

pages = Blueprint(__name__, "pages")

@pages.route("/")
def home():
    return render_template("index.html")

""" 
@pages.route("/aboutme")
def aboutme():
    return render_template("index.html")

@pages.route("/projects")
def projects():
    return render_template("index.html")

@pages.route("/contactme")
def contactme():
    return render_template("index.html")
""" 

# redirects are below

""" 
@pages.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@pages.route("/go-to-aboutme")
def go_to_aboutme():
    return redirect(url_for("views.aboutme"))

@pages.route("/go-to-contactme")
def go_to_contactme():
    return redirect(url_for("views.contactme"))
""" 
