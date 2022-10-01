from flask import Flask, render_template,session, redirect
app = Flask(__name__)
app.secret_key = 'asdfklja;lksdjfa;lkjfds'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=   0
    session['count'] += 1
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/plus2')
def plus2():
    session['count'] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)