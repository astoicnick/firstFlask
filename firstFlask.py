from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('test.db')

@app.route('/')
def home():
    return render_template("test.html")
@app.route('/handle_data', methods=['POST'])
def handle_data():
    return render_template("submitted.html", testText = request.form['email2'])

if __name__ == "__main__":
    app.run(debug=True,port=8080)