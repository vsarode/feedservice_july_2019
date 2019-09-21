from feed_service_july_2019.utils.answer import get_answer_dict


def get_upvote_dict(upvote_object):
    return {"answer": upvote_object.answer.a_string,
            'createdBy': upvote_object.created_by,
            'id': upvote_object.id}
