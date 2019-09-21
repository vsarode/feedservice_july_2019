from feed_service_july_2019.db.feed_models.models import Answer, Upvote


def create_upvote(data):
    try:
        answer_object = Answer.objects.get(id=data['answer'])
    except:
        print
        return None

    upvote_object = Upvote.objects.create(answer=answer_object,
                                          created_by=data['createdBy'])
    return upvote_object


def get_upvote(filter):
    criteria = {}
    if 'createdBy' in filter:
        criteria['created_by'] = filter['createdBy']
    if 'answer' in filter:
        criteria['answer_id'] = filter['answer']
    return Upvote.objects.filter(**criteria)
