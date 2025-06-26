from flask import Flask, render_template, request, redirect
from database import get_connection, init_db

app=Flask(__name__)

init_db

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/add',methods=['POST'])
def add_job():
    company = request.form['company']
    position = request.form['position']
    date_applied = request.form['date_applied']
    status = request.form['status']

    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO jobs (company, position, date_applied, status) VALUES (?,?,?,?)",
              (company, position, date_applied, status))
    conn.commit()
    conn.close()

    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)