import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for flash messages

# Database configuration (you can store these as env variables)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'avenir_db'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone', '')
        message = request.form['message']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO contact (name, email, phone, message) VALUES (%s, %s, %s, %s)"
            values = (name, email, phone, message)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            flash('Thank you! Your message has been sent.', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('contact'))

        return redirect(url_for('contact'))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)