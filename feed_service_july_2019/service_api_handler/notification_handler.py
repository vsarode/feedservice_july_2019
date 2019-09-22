from feed_service_july_2019.db.feed_models.models import Notification


def create_notification(type, entity_id, actioned_entity_id, done_by, owner):
    notification_object = Notification.objects.create(type=type, entity=entity_id,
                                                      actioned_entity=actioned_entity_id,
                                                      done_by=done_by, owner=owner)
    return notification_object


def get_notifications(data):
    criteria = {}
    if 'owner' in data:
        criteria['owner'] = data['owner']
    if 'isViewed' in data:
        criteria['is_viewed'] = data['isViewed']
    return Notification.objects.filter(**criteria)
