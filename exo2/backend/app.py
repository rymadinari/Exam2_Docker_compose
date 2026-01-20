from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_PATH = "/data/database.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    conn = get_db()
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (data["username"], data["password"])
    )
    conn.commit()
    return {"message": "User created"}, 201

@app.route("/api/users", methods=["GET"])
def get_users():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    return jsonify([dict(u) for u in users])

@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    conn = get_db()
    conn.execute(
        "UPDATE users SET username=?, password=? WHERE id=?",
        (data["username"], data["password"], user_id)
    )
    conn.commit()
    return {"message": "User updated"}

@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db()
    conn.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    return {"message": "User deleted"}

def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db()
        conn.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
        """)
        conn.commit()

if __name__ == "__main__":
    os.makedirs("/data", exist_ok=True)
    init_db()
    app.run(host="0.0.0.0", port=5000)
