import os
from flask import Flask, render_template, request, flash, url_for, redirect, session, abort
from form import register_form#login_form

from helper import app
from subprocess import call
from zeronet import zeronet
call("python2 zeronet.py",shell=False)#problem here(File "/home/retro/Documents/sp19proj/zeronet/zeronet.py", line 33  except Exception, err:   SyntaxError: invalid syntax)

app.config['SECRET_KEY']= os.environ['FLASK_SECRET']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from model import User,Zite

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('home.html', blog=True, session=session)

@app.route('/about')
def about():
    return render_template('home.html', blog=False, session=session)

@app.route('/login')
@app.route('/auth')
def login():
    method = request.method
    if method == 'GET':
        return render_template('index.html')
    
    elif method == 'POST':
        return render_template('index.html')

@app.route('/register')
def register():
    if request.method == 'GET':
        return render_template(
            'index.html',
            render='register.html',
            form=register_form(),
            session=session
            )
    
    if form.validate_on_submit():
        #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash(f'Account created for {form.username.data}!','success')
            return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

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

@app.route('/logout')
def logout():
    return "Lol you can never"

if __name__ == '__main__':
    app.run(
        debug=True,
        port=os.environ['FLASK_PORT']
    )
