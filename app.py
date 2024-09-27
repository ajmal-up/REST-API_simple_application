from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to my Flask REST API!")

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello Devloot!")

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f"Hello, {name}!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
