from flask import request, jsonify
from flask_restful import Resource

from feed_service_july_2019.service_api_handler import upvote_handler, downvote_handler
from feed_service_july_2019.utils.upvote import get_upvote_dict


class Downvote(Resource):
    def post(self):
        data = request.get_json()
        downvote_object = downvote_handler.create_downvote(data)
        if downvote_object:
            return jsonify({"upvote": get_upvote_dict(downvote_object)})
        else:
            return "<h1>Error while creating upvote!!</h1>"

    def get(self):
        filter = request.args
        upvote_objects = upvote_handler.get_upvote(filter)
        return jsonify({"upvotes": [get_upvote_dict(upvote) for upvote in upvote_objects]})
