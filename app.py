from flask import Flask, render_template
import psycopg2
from flask_wtf import FlaskForm

conn = psycopg2.connect("dbname=upgraded-happiness user='Bark Bark'")


app = Flask(__name__)


@app.route('/')
def hello_world():
    cur = conn.cursor()
    cur.execute("SELECT * FROM history;")
    exercises = cur.fetchall()
    cur.close()
    return render_template('main.html', exercises=exercises)

@app.route('/nami')
def nami():
    return "NAMI NAMI NAMI"

if __name__ == '__main__':
    app.run()
