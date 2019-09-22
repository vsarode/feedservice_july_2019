import django;


django.setup();
from flask import Flask
from flask_restful import Api

from feed_service_july_2019.service_apis.topic import Topic
from feed_service_july_2019.service_apis.question import Question
from feed_service_july_2019.service_apis.answer import Answer
from feed_service_july_2019.service_apis.upvote import Upvote
from feed_service_july_2019.service_apis.downvote import Downvote
from feed_service_july_2019.service_apis.notification import Notification
from feed_service_july_2019.service_apis.ping import Ping


app = Flask(__name__)

api = Api(app, prefix='/feedservice/')

api.add_resource(Ping, 'ping')
api.add_resource(Topic, 'topic')
api.add_resource(Question, 'question')
api.add_resource(Answer, 'answer')
api.add_resource(Upvote, 'upvote')
api.add_resource(Downvote, 'downvote')
api.add_resource(Notification, 'notification')

if __name__ == '__main__':
    app.run(host='localhost', port=2005, debug=True)
