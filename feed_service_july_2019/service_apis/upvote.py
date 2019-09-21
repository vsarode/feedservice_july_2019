from flask import request, jsonify
from flask_restful import Resource

from feed_service_july_2019.service_api_handler import upvote_handler
from feed_service_july_2019.utils.upvote import get_upvote_dict


class Upvote(Resource):
    def post(self):
        data = request.get_json()
        upvote_object = upvote_handler.create_upvote(data)
        print upvote_object
        if upvote_object:
            return jsonify({"upvote": get_upvote_dict(upvote_object)})
        else:
            return "<h1>Error while creating upvote!!</h1>"

    def get(self):
        filter = request.args
        upvote_objects = upvote_handler.get_upvote(filter)
        return jsonify({"upvotes": [get_upvote_dict(upvote) for upvote in upvote_objects]})
