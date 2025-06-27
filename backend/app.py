from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

DB_HOST = os.environ.get('DB_HOST', 'db')
DB_NAME = os.environ.get('DB_NAME', 'art_portfolio')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS artworks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT
);
""")
conn.commit()


@app.route('/api/artworks', methods=['GET'])
def get_artworks():
    cursor.execute("SELECT * FROM artworks;")
    artworks = cursor.fetchall()
    return jsonify([
        {"id": row[0], "title": row[1], "description": row[2]} for row in artworks
    ])


@app.route('/api/artworks', methods=['POST'])
def add_artwork():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title:
        return jsonify({"error": "Title is required"}), 400

    cursor.execute("INSERT INTO artworks (title, description) VALUES (%s, %s) RETURNING id;",
                   (title, description))
    new_id = cursor.fetchone()[0]
    conn.commit()
    return jsonify({"id": new_id, "title": title, "description": description}), 201


@app.route('/api/artworks/<int:artwork_id>', methods=['DELETE'])
def delete_artwork(artwork_id):
    cursor.execute("DELETE FROM artworks WHERE id = %s;", (artwork_id,))
    conn.commit()
    return jsonify({"message": "Artwork deleted"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
