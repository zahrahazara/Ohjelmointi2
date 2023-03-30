from flask import Flask, jsonify

app = Flask(__name__)

# Lataa lentokenttätietokanta
kentat = {
    "EFHK": {"ICAO": "EFHK", "Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"}
}

@app.route('/kenttä/<icao>', methods=['GET'])
def hae_kentta(icao):
    try:
        kentta = kentat[icao]
        return jsonify(kentta)
    except :
        return jsonify({"error": "Kenttää ei löytynyt."}), 404

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Sivua ei löydy."}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


