from app import db, ma
from app.models import users, coins

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = users
