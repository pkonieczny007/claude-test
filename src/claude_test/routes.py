from flask import Flask, jsonify, render_template


def register_routes(app: Flask):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

    @app.route("/settings", methods=["GET", "POST"])
    def settings():
        return render_template("settings.html")

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})
