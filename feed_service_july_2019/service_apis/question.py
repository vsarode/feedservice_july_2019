from flask import request, jsonify
from flask_restful import Resource

from feed_service_july_2019.service_api_handler import question_handler
from feed_service_july_2019.utils.question import get_question_dict


class Question(Resource):
    def post(self):
        data = request.get_json()
        question_object = question_handler.create_question(data)
        return jsonify({"question": get_question_dict(question_object)})

    def get(self):
        filter = request.args
        question_objects = question_handler.get_question_by_filter(filter)
        return ({"questions": [get_question_dict(q) for q in question_objects]})