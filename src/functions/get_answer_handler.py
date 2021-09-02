import json
from src.functions.handlers_view import HandlersView


class Init:
    view = HandlersView()


def handle(event, context):
    print(f'Event:\n{event}')
    path_params = event.get("pathParameters", {}) or {}

    if "answer_id" not in path_params or not ("question_id" in path_params and "candidate_id" in path_params):
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Missing question id"})
        }
    question_id = path_params.get("question_id", None)
    answer_id = path_params.get("answer_id", None)
    candidate_id = path_params.get("answer_id", None)
    answered_question = Init.view.get_answered_question(answer_id=answer_id, candidate_id=candidate_id,
                                                        question_id=question_id)
    return {
        "statusCode": 200,
        "body": json.dumps(answered_question)
    }
