from flask import Flask, jsonify, request
import subprocess
import json

app = Flask(__name__)

# Load konfigurasi
with open("config.json", "r") as f:
    config = json.load(f)

# Route untuk cek status IPTables
@app.route("/iptables/status", methods=["GET"])
def get_iptables_status():
    try:
        result = subprocess.run(["iptables", "-L", "-v", "-n"], capture_output=True, text=True)
        return jsonify({"status": "success", "output": result.stdout})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"], debug=True)
