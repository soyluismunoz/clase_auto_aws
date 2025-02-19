from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/users', methods=['GET'])
def users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}, 
        {"id": 3, "name": "Charlie"}
    ]
    return jsonify({"users": users})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK", "version": "1.0"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
