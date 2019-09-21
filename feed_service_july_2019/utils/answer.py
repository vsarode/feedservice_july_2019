def get_answer_dict(answer_object):
    return {"aString": answer_object.a_string,
            "id": answer_object.id,
            "question": answer_object.question.q_string,
            "createdBy": answer_object.created_by,
            "createdOn": answer_object.created_on.strftime('%d/%m/%Y')}
