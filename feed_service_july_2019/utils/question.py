from feed_service_july_2019.utils.topic import get_topic_dict


def get_question_dict(question_object):
    return {"qString": question_object.q_string,
            "id": question_object.id,
            "createdBy": question_object.created_by,
            "createdOn": question_object.created_on.strftime("%d/%m/%Y"),
            "topic": get_topic_dict(question_object.topic)
            }
