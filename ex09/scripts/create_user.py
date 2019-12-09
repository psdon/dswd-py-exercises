def create_user(db, Model):
    user = Model(username="admin", email="admin@mail.com", password="admin")
    db.session.add(user)
    db.session.commit()


from dswd_blog.extensions import db
from dswd_blog.models import User
from scripts.create_user import create_user
create_user(db, User)