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
    question = Init.view.get_candidate_question(question_id=question_id)
    return {
        "statusCode": 200,
        "body": json.dumps(question)
    }
