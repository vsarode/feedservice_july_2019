from feed_service_july_2019.db.feed_models.models import Question, Topic


def create_question(data):
    try:
        topic_object = Topic.objects.get(id=data['topic'])
    except:
        return None
    question_object = Question.objects.create(q_string=data['qString'],
                                              created_by=data['username'],
                                              topic=topic_object)
    return question_object


def get_question_by_filter(filter):
    criteria = {}
    if 'createdBy' in filter:
        criteria['created_by']=filter['createdBy']
    if 'topic' in filter:
        criteria['topic_id'] =filter['topic']
    return Question.objects.filter(**criteria)
