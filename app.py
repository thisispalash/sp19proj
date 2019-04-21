import os
from flask import Flask, render_template, request, flash, url_for, redirect
from form import register_form#login_form

from helper import app

app.config['SECRET_KEY']= os.environ['FLASK_SECRET']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from model import User,Zite


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('home.html', blog=True)

@app.route('/about')
def about():
    return render_template('home.html', blog=False)

@app.route('/login')
@app.route('/auth')
def login():
    method = request.method
    if method == 'GET':
        return render_template('index.html')
    
    elif method == 'POST':
        return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form=register_form()
    if form.validate_on_submit():
        #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('login'))
    return render_template('register.html',title= 'Register',form=form)

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
    

@app.route('/contact')
def contact():
    return "Coming soon"

if __name__ == '__main__':
    app.run(
        debug=True,
        port=os.environ['FLASK_PORT']
    )
