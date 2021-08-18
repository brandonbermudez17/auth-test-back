from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene
from models import User

class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = User
       interfaces = (graphene.relay.Node, )