from .base import Model
from back_end.app.extensions import db
from back_end.app.common.helpers import get_slug
from back_end.app.constants import models


class Topics(Model):
    name = db.Column(db.String(length=models.NAME_LENGTH['MAX']), nullable=False)
    slug = db.Column(db.String(length=models.NAME_LENGTH['MAX']), default=get_slug)
    sticky = db.Column(db.Boolean, default=False)
    views = db.Column(db.Integer, default=0)
    description = db.Column(db.Text)

    # author = db.relationship('Users', backref=db.backref('topics', lazy='dynamic'))
    # author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    category = db.relationship('Categories', backref=db.backref('topics', lazy='dynamic'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
