from flask.json import JSONEncoder as BaseJSONEncoder

from back_end.app.extensions import db
from back_end.app.common.helpers import get_current_date
from flask_sqlalchemy import declared_attr, declarative_base


class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """

    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
        return super(JSONEncoder, self).default(obj)


class JsonSerializer(object):
    # get record's fields
    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    # convert record to dictionary
    def to_dict(self, *args, **kwargs):
        result = dict()
        for key in self.__table__.columns.keys():
            result[key] = getattr(self, key)
        return result


class Base(JsonSerializer):
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    def __repr__(self):
        return '<{} (id: {})>'.format(self.__class__.__name__, self.id)

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=get_current_date())
    updated_at = db.Column(db.DateTime, default=get_current_date())
    deleted = db.Column(db.Boolean, default=False)


Model = db.make_declarative_base(model=Base)
