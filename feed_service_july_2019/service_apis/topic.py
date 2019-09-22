from flask import request, jsonify
from flask_restful import Resource

from feed_service_july_2019.service_api_handler import topic_handler
from feed_service_july_2019.services.user_service import get_user_data_from_user_service
from feed_service_july_2019.utils.topic import get_topic_dict


class Topic(Resource):
    def post(self):
        token = request.cookies.get("token")
        if token:
            user_data = get_user_data_from_user_service(token)
        else:
            raise Exception
        print type(user_data)
        data = request.get_json()
        data['createdBy'] = user_data['user']['userName']
        topic_object = topic_handler.create_topic(data)
        return jsonify({"topic": get_topic_dict(topic_object)})

    def get(self):
        filter = request.args
        topics = topic_handler.get_topic_by_filter(filter)
        return jsonify({"topics": [get_topic_dict(t) for t in topics]})

    