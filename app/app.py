from flask import Flask, render_template_string
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.environ.get("DB_HOST"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME")
}

@app.route("/")
def home():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM messages LIMIT 1;")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template_string(
        "<h1>Two Tier Web App</h1><p>{{msg}}</p>",
        msg=result[0]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
