import os
import subprocess

from flask import Flask, render_template, request, flash, url_for, redirect, session, abort
from form import register_form#login_form

from helper import app

zeronet = 'python2 zeronet/zeronet.py'
process = subprocess.Popen(zeronet.split(),stdout=subprocess.PIPE)
out,err = process.communicate()

from model import User,Zite

# Sorry
users = {}
user_count = 1
# Not sorry


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('home.html', blog=True, session=session)

@app.route('/about')
def about():
    return render_template('home.html', blog=False, session=session)

@app.route('/login', methods=['GET','POST'])
@app.route('/auth', methods=['GET','POST'])
def login():
    from form import login_form
    form = login_form()
    method = request.method
    if request.method == 'GET':
        return render_template(
        'index.html',
        render='login.html',
        form=form
        )
    # TODO Check and redirect post
    # global users
    # print(users)
    # print(form.data)
    # for id,user in users.items():
    #     if user['username'] == form.data['username']:
    #         if user['priv'] == form.data['priv']:
    #             return 'welcome '+user['name']
    # return 'invalid login'

@app.route('/register', methods=['GET','POST'])
def register():
    from form import register_form
    form = register_form()
    if request.method == 'GET':
        pub,priv = get_new_keypair()
        return render_template(
            'index.html',
            render='register.html',
            form=form,
            session=session,
            pub=pub, priv=priv
            )
    # TODO: Check and save to db
    # global users, user_count
    # print(users)
    # users[user_count] = {
    #     'name': form.data['name'],
    #     'username': form.data['username'],
    #     'pub': form.data['pub'],
    #     'priv': form.data['priv']
    # }
    # user_count+=1
    # print(users)
    # return redirect('login')

@app.route('/browse')
def browse():
    cmd = 'python2 zeronet/zeronet.py --silent'
    process = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE)
    out,err = process.communicate()
    return render_template('browse.html', redirect_uri='http://127.0.0.1:43110')

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
    session.clear()
    return redirect('/auth')


''' Helpers '''
def get_new_keypair():
    cmd = 'python2 zeronet/PubPriv.py new'
    process = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE)
    out,err = process.communicate()
    out = out.decode()
    pair = out.split('\n') #TODO Add error checking
    return pair[0],pair[1]

if __name__ == '__main__':
    app.run(
        debug=True,
        port=os.environ['FLASK_PORT']
    )
