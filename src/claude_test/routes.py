from flask import Flask, jsonify, render_template, request

from claude_test.models import User, db


def register_routes(app: Flask):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():
        user_count = User.query.count()
        return render_template("dashboard.html", user_count=user_count)

    @app.route("/settings", methods=["GET", "POST"])
    def settings():
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            theme = request.form.get("theme", "light")
            if username:
                user = User.query.filter_by(username=username).first()
                if user:
                    user.theme = theme
                else:
                    user = User(username=username, theme=theme)
                    db.session.add(user)
                db.session.commit()
                return render_template(
                    "settings.html", user=user, saved=True
                )
        return render_template("settings.html")

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})
