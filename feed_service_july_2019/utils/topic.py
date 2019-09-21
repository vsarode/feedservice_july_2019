def get_topic_dict(topic_object):
    return {"name": topic_object.name,
            "id": topic_object.id,
            "createdBy": topic_object.created_by,
            "createdOn": topic_object.created_on.strftime("%d/%m/%Y")}
