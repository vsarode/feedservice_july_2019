from feed_service_july_2019.db.feed_models.models import Topic


def create_topic(data):
    topic_object = Topic.objects.create(name=data['name'], created_by=data['username'])
    return topic_object


def get_topic_by_filter(filter={}):
    criteria = {}
    if 'createdBy' in filter:
        criteria['created_by'] = filter['createdBy']
    if 'id' in filter:
        criteria['id'] = filter['topic']
    return Topic.objects.filter(**criteria)
