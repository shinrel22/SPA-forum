from .base import Model, Base
from back_end.app.extensions import db
from back_end.app.common.helpers import get_slug
from back_end.app.constants import models


class Groups(Model):
    name = db.Column(db.String(length=models.NAME_LENGTH['MAX']), nullable=False)
    slug = db.Column(db.String(length=models.NAME_LENGTH['MAX']), default=get_slug)
    description = db.Column(db.Text)
