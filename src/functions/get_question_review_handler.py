import json
from src.functions.handlers_view import HandlersView


class Init:
    view = HandlersView()


def handle(event, context):
    print(f'Event:\n{event}')
    path_params = event.get("pathParameters", {}) or {}

    if "questionId" not in path_params:
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Missing question id"})
        }
    question_id = path_params.get("questionId", None)
    question_review = Init.view.get_question_review(question_id=question_id)
    return {
        "statusCode": 200,
        "body": json.dumps(question_review)
    }
