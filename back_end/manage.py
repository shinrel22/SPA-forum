import slugify
from flask_script import Manager, Shell, Server
from flask import current_app
from back_end.app.app import create_app
from back_end.app.chosen_config import CHOSEN_CONFIG
from back_end.app.extensions import db
from back_end.seed import *
from back_end.app.models import Categories, Groups, Model

app = create_app(CHOSEN_CONFIG)

manager = Manager(app)

# runs Flask development server locally at port 5000
manager.add_command('runserver', Server(host='0.0.0.0', port=5000))


def query_with_relates(query, relates):
    if not relates:
        return query
    return query_with_relates(query.outerjoin(relates.pop(0)).filter_by(**{}), relates)


# start a Python shell with contexts of the Flask application
@manager.shell
def make_shell_context():
    return dict(app=current_app, db=db, init_db=init_db,
                Categories=Categories, Groups=Groups, Model=Model,
                query_with_relates=query_with_relates)


@manager.command
def init_db():
    db.drop_all()
    db.create_all()

    # create groups and categories
    for group in groups:
        new_group = Groups(name=group['name'])
        db.session.add(new_group)
        db.session.commit()

        for category in group['categories']:
            new_category = Categories(name=category['name'])
            db.session.add(new_category)
            db.session.commit()


if __name__ == '__main__':
    manager.run()
