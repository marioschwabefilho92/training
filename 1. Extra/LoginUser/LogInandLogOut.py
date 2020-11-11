from flask import Flask, render_template, request, escape, session

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'mario',
                          'database': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


@app.route('/', methods=['GET', 'POST'])
def check_login() -> 'html':
    return render_template('entry.html', the_title='Please do your Login!')

@app.route('/showlog', methods=['GET', 'POST'])
def print_user() -> str:
    username = request.form['username']
    password = request.form['password']
    return render_template('user.html', the_title='Please do your Login!', the_username = username, the_password = password)

app.secret_key = 'MarioSchwabeFilho'

if __name__ == '__main__':
    app.run(debug=True)
