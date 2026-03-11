from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

    @app.route("/story")
    def story():
        return render_template("story.html")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)