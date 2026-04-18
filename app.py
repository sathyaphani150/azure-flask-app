from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Sample in-memory data
users = [
    {"name": "Jack", "role": "Developer"},
    {"name": "Alice", "role": "Tester"},
    {"name": "Bob", "role": "Manager"}
]

@app.route("/")
def home():
    return jsonify({"message": "Flask App Running Successfully"})

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added", "data": data}), 201

@app.route("/users/<int:index>", methods=["DELETE"])
def delete_user(index):
    if index < len(users):
        deleted = users.pop(index)
        return jsonify({"message": "User deleted", "data": deleted})
    return jsonify({"error": "User not found"}), 404

@app.route("/env")
def get_env():
    return jsonify({
        "APP_NAME": os.getenv("APP_NAME"),
        "ENV": os.getenv("ENV"),
        "CUSTOM_MESSAGE": os.getenv("CUSTOM_MESSAGE")
    })

if __name__ == "__main__":
    app.run(debug=True)