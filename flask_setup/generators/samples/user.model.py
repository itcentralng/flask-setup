class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    role = db.Column(db.String, nullable=True)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    
    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def generate_token(self):
        payload = {
            'exp': app.config.get('JWT_REFRESH_TOKEN_EXPIRES'),
            'iat': datetime.utcnow(),
            'sub': self.id,
            'role': self.role
        }
        return jwt.encode(payload, secret, algorithm='HS256')
    
    def generate_password(self):
        """
        It generates a random password of length 10 using the string module and the secrets module
        :return: A string of 10 characters, with each character being randomly selected from the alphabet.
        """
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        return password
    
    def update_password(self, old_password, new_password):
        if self.is_verified(old_password):
            self.password = new_password
            self.hash_password()
            return self.update()
        return False
    
    def update(self):
        try:
            db.session.commit()
            return True
        except:
            return False
    
    @classmethod
    def get_by_email(self, email):
        return User.query.filter(User.email).first()