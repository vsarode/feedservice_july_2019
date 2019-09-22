from flask_restful import Resource


class Ping(Resource):
    def get(self):
        return " Feed service UP!!!!"