import graphene
from flask import Flask
from mutations import Mutation
from queries import Query
from flask_graphql import GraphQLView

def create_app() -> Flask :

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/auth_test.db'
    app.config['SECRET_KEY'] = 'test-jwt-brandon'
    app.config["JWT_SECRET_KEY"] = "test-jwt-brandon"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    initialize_app(app)

    schema = graphene.Schema(query=Query, mutation=Mutation)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )
    return app

def initialize_app(app: Flask):
    from extensions import db, auth, cors
    db.init_app(app)
    auth.init_app(app)
    cors.init_app(app)

    with app.app_context():
        db.create_all()