from flask import Flask, jsonify, request
import deepcut
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    q = request.args.get('q')
    return jsonify(data=deepcut.tokenize(q))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)