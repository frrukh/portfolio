from flask import Flask, render_template, request, redirect, url_for, flash
from mysql.connector import connect

app = Flask(__name__)
connection = connect(host='localhost', user='root', password='', database='portfolio')
app.secret_key = 'kldfj239ruf20jsefiu3298fajlfj2903lsdfjoaweifj923890fjfoajwevslkjvd'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register/contact', methods=['POST'])
def contactMe():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    if name and email and message:
        db = connection.cursor()
        db.execute('INSERT INTO contact (name, email, message) VALUES(%s, %s, %s)',(name, email, message))
        connection.commit()
        db.close()
        flash('Your message was sent successfully!', 'success')
        return redirect( url_for('home') )
    else:
        flash('Please make sure that you have filled all the entries!', 'danger')
        return redirect( url_for('home') )


if __name__ == '__main__':
    app.run(port=8000, debug=True)