from flask import Flask, jsonify


def register_routes(app: Flask):
    @app.route("/")
    def index():
        return jsonify({"message": "Hello from claude-test!"})

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})
