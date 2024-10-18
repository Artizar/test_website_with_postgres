from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# PostgreSQL connection setup
conn = psycopg2.connect(
    host="localhost",  # Update with your host, typically "localhost"
    database="simple_website",  # The name of the database created above
    user="postgres",  # Replace with your PostgreSQL user
    password="admin123"  # Replace with your PostgreSQL password
)
cur = conn.cursor()

@app.route('/')
def index():
    cur.execute("SELECT * FROM users")
    print('yai, "select * from users succes"') #test if the select * from users is working or not
    users = cur.fetchall()  # Fetch all users from the "users" table
    print('yeah user = cur.fetchall succed') #test if get through or not
    print(users)  # test output
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
