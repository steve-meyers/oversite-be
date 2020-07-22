from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    street_address = db.Column(db.String())
    state = db.Column(db.String())
    zip = db.Column(db.String())

    def __init__(self, first_name, last_name, email, street_address, state, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.street_address = street_address
        self.state = state
        self.zip = zip

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'street_address': self.street_address,
            'state': self.state,
            'zip': self.zip
        }