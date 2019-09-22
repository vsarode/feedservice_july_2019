from flask import jsonify

from feed_service_july_2019.constants import notification_constants
from feed_service_july_2019.db.feed_models.models import Question, Answer
from feed_service_july_2019.service_api_handler import notification_handler
from feed_service_july_2019.utils.answer import get_answer_dict


def create_answer(data):
    answer = data['answer']
    question = int(data['question'])
    createdby = data['creatdBy']

    answer_object = Answer.objects.filter(a_string=answer, question_id=question)
    # print answer_object[0].__dict__
    if answer_object:
        return "<h1>answer already exists</h1>"
    try:
        question_object = Question.objects.get(id=question)
        answer_object = Answer.objects.create(a_string=answer, question=question_object, created_by=createdby)
    except:
        return "<h1>question does not exists</h1>"

    notification_handler.create_notification(notification_constants.TYPE_ANSWER,
                                             answer_object.id, question_object.id,
                                             createdby, question_object.created_by)
    return jsonify({"answer": get_answer_dict(answer_object)})


def get_answer_by_filter(filter):
    criteria = {}
    if 'createdBy' in filter:
        criteria['created_by'] = filter['createdBy']
    if 'question' in filter:
        criteria['question_id'] = filter['question']
    return Answer.objects.filter(**criteria)
