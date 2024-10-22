from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def home():
  username = request.cookies.get('username')
  if username:
    return render_template('index.html', username=username)
  return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('username', username)
    return resp
  return render_template('login.html')

@app.route('/logout')
def logout():
  resp = make_response(redirect(url_for('login')))
  resp.set_cookie('username', '', expires=0)
  return resp

if __name__ == '__main__':
  app.run(debug=True)
