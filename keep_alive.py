from flask import Flask, jsonify, send_file
from threading import Thread
import os
from dotenv import load_dotenv

load_dotenv()

db_folder = os.getenv("DB_PATH").split('/')[0]
db_name = os.getenv("DB_PATH").split('/')[1]

app = Flask(__name__)

@app.route('/')
def index():
    return "Server is alive!"

@app.route('/get_db_file')
def get_db_file():
    db_path = os.path.join(os.getcwd(), db_folder, db_name)
    if os.path.exists(db_path):
        return send_file(db_path, as_attachment=True)
    else:
        return jsonify({"error": "Database file not found"}), 404

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
