import os

from flask import Flask, render_template, request
# from form import register#login
app = Flask(__name__)

app.config['SECRET_KEY']= os.environ['FLASK_SECRET']

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('home.html', blog=True)

@app.route('/about')
def about():
    return render_template('home.html', blog=False)

@app.route('/auth')
def login():
    method = request.method
    if method == 'GET':
        return render_template('index.html')
    
    elif method == 'POST':
        return render_template('index.html')

@app.route('/register')
def register():
    form=register()
    return render_template('register.html',title= 'Register',form='form')

@app.route('/browse')
def browse():
    # TODO: Browse the zeronet
    return render_template('browse.html')

@app.route('/create')
@app.route('/update')
@app.route('/update/<pub>')
def zerosite(pub):
    method = request.method
    # TODO
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(
        debug=True,
        port=os.environ['FLASK_PORT']
    )
