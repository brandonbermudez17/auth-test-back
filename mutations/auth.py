import graphene
from flask_graphql_auth import (create_access_token, create_refresh_token)
from models import User

class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()
    
    def mutate(self, info , username, password) :
        user = User.query.filter_by(username=username,password=password).first()
        print(user)
        if not user:
            raise Exception('Authenication Failure : User is not registered')
        return AuthMutation(
            access_token = create_access_token(username),
            refresh_token = create_refresh_token(username)
        )