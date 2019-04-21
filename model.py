from helper import db,login_manager

# TODO: Init db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    zites = db.relationship('Zite',backref='author',lazy=True)  #1 to many relationship with zite

    def __repr__(self):
        return f"User('{self.username}')"

class Zite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, default='website')
    #zip file from user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"User('{self.title}')" #also print the zip file
        