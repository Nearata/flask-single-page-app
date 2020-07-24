from flask import Blueprint, render_template

bp = Blueprint("main", __name__, static_folder="../static", template_folder="../templates")


@bp.route("/", defaults={"path": "/"})
@bp.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")
