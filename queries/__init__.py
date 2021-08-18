import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from schemas.user import UserObject
from models import User
from flask_graphql_auth import get_jwt_identity, query_jwt_required

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserObject)
    get_user = graphene.Field(type=UserObject, token=graphene.String())

    @query_jwt_required
    def resolve_get_user(self,info):
        current_user = get_jwt_identity()
        user_qry = UserObject.get_query(info)
        user = user_qry.filter(User.username.contains(current_user)).first()
        return user