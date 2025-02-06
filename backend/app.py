from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../frontend", static_url_path="")

# Rădăcina site-ului - servește index.html
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Rute pentru fișiere statice (CSS, JS, imagini)
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)