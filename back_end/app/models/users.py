from .base import Model
from back_end.app.extensions import db
from back_end.app.constants import models
from back_end.app.common.helpers import get_current_date


class Users(Model):
    username = db.Column(db.String(length=models.USERNAME_LENGTH['MAX']), nullable=False)
    email = db.Column(db.String(length=models.EMAIL_LENGTH['MAX']), nullable=False)
    phone = db.Column(db.String(length=models.PHONE_LENGTH['MAX']))
    fullname = db.Column(db.String(length=models.NAME_LENGTH['MAX']))
    avatar = db.Column(db.String(length=models.URL_LENGTH['MAX']))
    encrypted_password = db.Column(db.String(length=models.PASSWORD_LENGTH['MAX']), nullable=False)
    current_sign_in_at = db.Column(db.DateTime, default=get_current_date())
    last_sign_in_at = db.Column(db.DateTime, default=get_current_date())
    locked_at = db.Column(db.DateTime, default=None)
    current_sign_in_ip = db.Column(db.String(length=models.IP_LENGTH['MAX']))
    last_sign_in_ip = db.Column(db.String(length=models.IP_LENGTH['MAX']))
    sign_in_count = db.Column(db.Integer, default=0)
