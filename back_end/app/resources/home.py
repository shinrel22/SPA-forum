from flask_restful import Resource
from sqlalchemy.exc import *
from sqlalchemy import desc
from werkzeug.exceptions import *
from back_end.app.models import Categories, Groups, Topics
from back_end.app.extensions import db
from flask import make_response, request, abort, jsonify


class HomeResource(Resource):
    def get(self):
        pass

    def get_groups(self, *args, **kwargs):
        pass