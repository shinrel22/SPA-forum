from datetime import datetime
from slugify import slugify


def get_current_date():
    return datetime.utcnow


def get_slug(context):
    return slugify(context.current_parameters.get('name'))
