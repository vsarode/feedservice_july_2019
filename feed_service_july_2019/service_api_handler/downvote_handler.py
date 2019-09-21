from feed_service_july_2019.db.feed_models.models import Answer, Downvote


def create_downvote(data):
    try:
        answer_object = Answer.objects.get(id=data['answer'])
    except:
        print
        return None

    downvote_object = Downvote.objects.create(answer=answer_object,
                                              created_by=data['createdBy'])
    return downvote_object


def get_downvote(filter):
    criteria = {}
    if 'createdBy' in filter:
        criteria['created_by'] = filter['createdBy']
    if 'answer' in filter:
        criteria['answer_id'] = filter['answer']
    return Downvote.objects.filter(**criteria)
