from flask_sqlalchemy import SQLAlchemy
from flask_graphql_auth import GraphQLAuth
from flask_cors import CORS

db = SQLAlchemy()
auth = GraphQLAuth()
cors = CORS()
