from flask import request, jsonify
from flask_restful import Resource

from feed_service_july_2019.service_api_handler import answer_handler
from feed_service_july_2019.utils.answer import get_answer_dict


class Answer(Resource):
    def post(self):
        data = request.get_json()
        return answer_handler.create_answer(data)

    def get(self):
        filter = request.args
        answer_objects = answer_handler.get_answer_by_filter(filter)
        return jsonify({"answers": [get_answer_dict(a) for a in answer_objects]})
