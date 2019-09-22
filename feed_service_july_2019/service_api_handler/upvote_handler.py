from feed_service_july_2019.constants import notification_constants
from feed_service_july_2019.db.feed_models.models import Answer, Upvote
from feed_service_july_2019.service_api_handler import notification_handler


def create_upvote(data):
    try:
        answer_object = Answer.objects.get(id=data['answer'])
    except:
        print
        return None

    upvote_object = Upvote.objects.create(answer=answer_object,
                                          created_by=data['createdBy'])
    notification_handler.create_notification(notification_constants.TYPE_UPVOTE,
                                             upvote_object.id, answer_object.id,
                                             upvote_object.created_by,
                                             answer_object.created_by)
    return upvote_object


def get_upvote(filter):
    criteria = {}
    if 'createdBy' in filter:
        criteria['created_by'] = filter['createdBy']
    if 'answer' in filter:
        criteria['answer_id'] = filter['answer']
    return Upvote.objects.filter(**criteria)
