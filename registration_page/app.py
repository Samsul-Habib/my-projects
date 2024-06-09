from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the SQLite3 database
def init_sqlite_db():
    conn = sqlite3.connect('login.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT primary key, password TEXT, CONSTRAINT password_not_username CHECK (username != password))')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            with sqlite3.connect('login.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                return redirect(url_for('success'))
        except sqlite3.IntegrityError as e:
            msg = f"Error in insert operation: {e}"
        except Exception as e:
            conn.rollback()
            msg=f"Error in insert operation:{e}"
    return redirect(url_for('home'))
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
