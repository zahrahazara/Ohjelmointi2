import requests
from flask import Flask, jsonify
from math import sqrt

app = Flask(__name__)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
            if n % i == 0:
                return False
    return True

@app.route("/alkuluku/<int:n>")
def is_prime_route(n):
    try:
        prime = is_prime(n)
        response = {"number": n, "is prime": prime}
        return jsonify(response)
    except:
        return jsonify({"error": "virhelinen syöte."}), 400

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Sivua ei löydy."}), 404


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
