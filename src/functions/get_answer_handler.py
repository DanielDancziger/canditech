import json
from src.functions.handlers_view import HandlersView


class Init:
    view = HandlersView()


def handle(event, context):
    print(f'Event:\n{event}')
    path_params = event.get("pathParameters", {}) or {}

    if "answerId" not in path_params or not ("questionId" in path_params and "candidateId" in path_params):
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Missing question id"})
        }
    question_id = path_params.get("questionId", None)
    answer_id = path_params.get("answerId", None)
    candidate_id = path_params.get("candidateId", None)
    answered_question = Init.view.get_answered_question(answer_id=answer_id, candidate_id=candidate_id,
                                                        question_id=question_id)
    return {
        "statusCode": 200,
        "body": json.dumps(answered_question)
    }
