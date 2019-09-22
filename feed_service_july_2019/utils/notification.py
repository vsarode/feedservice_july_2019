from feed_service_july_2019.constants import notification_constants
from feed_service_july_2019.db.feed_models.models import Question, Answer

type_to_string_map = {notification_constants.TYPE_ANSWER: " has answered as ",
                      notification_constants.TYPE_UPVOTE: " has upvoted your ",
                      notification_constants.TYPE_DOWNVOTE: " has downvoted your "}


def get_notification_dict(notification_object):
    has_string = type_to_string_map[notification_object.type]

    if notification_object.type == notification_constants.TYPE_ANSWER:
        done_by = notification_object.done_by
        # has_string = " has answered your "

        question_object = Question.objects.get(id=notification_object.actioned_entity)
        question_string = question_object.q_string
        answer_object = Answer.objects.get(id=notification_object.entity)
        answer_string = answer_object.a_string
        return {"string": done_by + has_string + answer_string +" to your "+ question_string + " question.",
                "isViewed": notification_object.is_viewed, "owner": notification_object.owner,"type": notification_object.type}

    # if notification_object.type == notification_constants.TYPE_UPVOTE:
    #     has_string = " has upvoted your "
    # if notification_object.type == notification_constants.TYPE_DOWNVOTE:
    #     has_string = " has downvoted your "

    done_by = notification_object.done_by
    answer_object = Answer.objects.get(id=notification_object.actioned_entity)
    answer_string = answer_object.a_string
    return {"string": done_by + has_string + answer_string + " answer.", "isViewed": notification_object.is_viewed,
            "owner": notification_object.owner, "type": notification_object.type}
