from flask import request, jsonify
from flask_restful import Resource

from feed_service_july_2019.service_api_handler import notification_handler
from feed_service_july_2019.utils.notification import get_notification_dict


class Notification(Resource):
    def get(self):
        data = request.args
        notification_objects = notification_handler.get_notifications(data)
        return jsonify({"notifications": [get_notification_dict(n) for n in notification_objects]})
