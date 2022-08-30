from flask import Flask, jsonify
from func import func

app = Flask(__name__)


@app.route('/')
def main():
    return jsonify(func())


# @app.route('/data')
# def main1():
#     return jsonify(func())

if __name__ == '__main__':
    app.run(debug=True)
