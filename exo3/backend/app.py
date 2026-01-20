from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/api/users")
def users():
    try:
        proxies = {
            "http": "socks5h://tor:9050",
            "https": "socks5h://tor:9050"
        }

        r = requests.get(
            "https://randomuser.me/api/?results=5",
            proxies=proxies,
            timeout=60
        )

        r.raise_for_status()

        data = r.json()["results"]

        users = [
            {
                "name": f"{u['name']['first']} {u['name']['last']}",
                "picture": u["picture"]["medium"]
            }
            for u in data
        ]

        return jsonify(users)

    except Exception as e:
        print(" BACKEND ERROR:", e)
        return jsonify({
            "error": "Tor request failed",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
