from helper import db,login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(25), unique=True, nullable=False)
    pub = db.Column(db.String(34), unique=True, nullable=False)
    priv = db.Column(db.String(51), unique=True, nullable=False)
    zites = db.relationship('Zite',backref='author',lazy=True)  #1 to many relationship with zite

    def __repr__(self):
        return self.username

class Zite(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False, default='website')
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    addr = db.Column(db.String(34), unique=True, nullable=False)
    sec = db.Column(db.String(51), unique=True, nullable=False)
    data = db.Column(db.String(100), unique=True, nullable=False) # Datapath: 'data/user.pub/addr'
    def __repr__(self):
        return self.addr

def init_db():
    db.create_all()

    # Create a test user
    new_user = User('root@admin.test', '123456')
    new_user.display_name = 'Admin'
    db.session.add(new_user)
    db.session.commit()

    new_user.datetime_subscription_valid_until = datetime.datetime(2019, 5, 1)
    db.session.commit()

if __name__ == '__main__':
    init_db()