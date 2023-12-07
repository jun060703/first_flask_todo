from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')

users = {
    '123': generate_password_hash('123'),
    '234': generate_password_hash('123')
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username], password):
        session['username'] = username
        return redirect(url_for('index'))
    else:
        error_message = '맞지 않습니다. 다시 시도해주세요.'
        return render_template('coincideerror.html', error_message=error_message)

@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
