from flask import Flask, jsonify
import time

app = Flask(__name__)


@app.route("/igor", methods=["GET"])
def get():
    time.sleep(34)
    return jsonify({"msg": "Igor"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051, debug=True)
    print('hey')