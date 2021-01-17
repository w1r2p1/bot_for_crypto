from app import db

class users(db.Model):
    __tablename__ = "users"

    UId = db.Column(db.Integer, primary_key=True, nullable=False)
    UTGId = db.Column(db.String, nullable=False, unique=True)
    UNotificationInterval = db.Column(db.Integer, default=10)
    UFirstUseDatetime = db.Column(db.DateTime)
    ULastUseDatetime = db.Column(db.DateTime)

    def __repr__(self):
        return "<user %r>" % self.UTGId


class coins(db.Model):
    __tablename__ = "coins"

    CoinID = db.Column(db.Integer, primary_key=True, nullable=False)
    CoinName = db.Column(db.Integer, primary_key=True, nullable=False)
    UTGId = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return "<coinName %r>" % self.CoinName