import jwt, string, secrets, bcrypt
from datetime import datetime
from app import app, db, secret

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    role = db.Column(db.String, nullable=True)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        self.updated_at = db.func.now()
        db.session.commit()
    
    def generate_password(self):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        return password
    
    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def generate_refresh_token(self):
        return create_refresh_token(self.id)
    
    def generate_access_token(self):
        return create_access_token(identity=self.id, fresh=True, additional_claims={"role": self.role})
    
    def generate_refreshed_access_token(self):
        return create_access_token(identity=self.id, fresh=False, additional_claims={"role": self.role})
    
    def update_password(self, old_password, new_password):
        if self.is_verified(old_password):
            self.password = new_password
            self.hash_password()
            self.update()
            return True
        return False
    
    def reset_password(self, new_password):
        self.password = new_password
        self.hash_password()
        self.update()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def get_by_username(self, username):
        return User.query.filter(User.username==username).first()
    
    @classmethod
    def create(cls, username, password, role):
        user = cls(username=username, password=password, role=role)
        user.hash_password()
        user.save()
        return user