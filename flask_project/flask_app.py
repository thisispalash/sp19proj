from flask import Flask, render_template, request
# from form import register#login
app = Flask(__name__)

app.config['SECRETE_KEY']= '4fa371198aeace66523b19ddc73fc6e7'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    #return "<h1>Team:</h1>"
    return render_template('index.html')

@app.route('/auth')
def auth():
    return "<h1>Login & Management</h1>"

# @app.route('/register')
# def register():
#     form=register()
#     return render_template('register.html',title= 'Register',form='form')

# @app.route('/login')
# def login():
#     form=login()
#     return render_template('login.html',title= 'Login',form=form')

@app.route('/browse')
def browse():
    return render_template('navbar.html')
    
if (__name__ == "__main__"):
    app.run(debug=True)
    
