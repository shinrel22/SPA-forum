from .base import Model
from back_end.app.extensions import db
from back_end.app.common.helpers import get_slug
from back_end.app.constants import models


class Categories(Model):
    name = db.Column(db.String(length=models.NAME_LENGTH['MAX']), nullable=False)
    slug = db.Column(db.String(length=models.NAME_LENGTH['MAX']), default=get_slug)
    icon = db.Column(db.String(length=models.ICON_LENGTH['MAX']))
    description = db.Column(db.Text)

    group = db.relationship('Groups', backref=db.backref('categories', lazy='dynamic'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
