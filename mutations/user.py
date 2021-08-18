import graphene
from models import User
from extensions import db
from schemas.user import UserObject

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserObject)
    
    class Arguments:
        username =graphene.String(required=True)
        password =graphene.String(required=True)
        email =graphene.String(required=True)
    
    def mutate(self, info, username, password , email):
        user = User.query.filter_by(username=username).first()
        if user:
            return CreateUser(user=user)
        user = User(username=username,password=password,email=email)
        if user:
            db.session.add(user)
            db.session.commit()
        return CreateUser(user=user)