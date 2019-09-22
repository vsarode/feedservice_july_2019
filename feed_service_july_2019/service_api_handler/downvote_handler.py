from feed_service_july_2019.constants import notification_constants
from feed_service_july_2019.db.feed_models.models import Answer, Downvote
from feed_service_july_2019.service_api_handler import notification_handler


def create_downvote(data):
    try:
        answer_object = Answer.objects.get(id=data['answer'])
    except:
        print
        return None

    downvote_object = Downvote.objects.create(answer=answer_object,
                                              created_by=data['createdBy'])
    notification_handler.create_notification(notification_constants.TYPE_DOWNVOTE,
                                             downvote_object.id, answer_object.id,
                                             downvote_object.created_by, answer_object.created_by)
    return downvote_object


def get_downvote(filter):
    criteria = {}
    if 'createdBy' in filter:
        criteria['created_by'] = filter['createdBy']
    if 'answer' in filter:
        criteria['answer_id'] = filter['answer']
    return Downvote.objects.filter(**criteria)
