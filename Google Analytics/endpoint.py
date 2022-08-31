from flask import Flask, jsonify

from tests import check

app = Flask(__name__)


@app.route('/')
def main():
    return jsonify(check())


if __name__ == '__main__':
    app.run(debug=False)
