from mutations.auth import AuthMutation
from mutations.user import CreateUser
from mutations.refresh import RefreshMutation
from graphene import ObjectType

class Mutation(ObjectType):
    create_user = CreateUser.Field()
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()