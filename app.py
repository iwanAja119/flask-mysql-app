import os
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

# Terhubung ke MySQL XAMPP lewat host Docker internal
DB_HOST = os.environ.get("DB_HOST", "host.docker.internal")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ.get("DB_NAME", "praktikum_cc")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users;")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({
            "status": "success",
            "message": "Berhasil terhubung ke MySQL XAMPP!",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Gagal terhubung ke MySQL XAMPP",
            "error_detail": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
