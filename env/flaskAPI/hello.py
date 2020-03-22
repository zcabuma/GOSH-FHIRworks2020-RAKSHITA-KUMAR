from flask import Flask, escape, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"about": 'Hello World'})


if __name__ == '__main__':
    app.run(debug = True)