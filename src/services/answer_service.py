from src.db.dynamo_helper import DynamoDBService
from src.db.tables import AnswerTable


class AnswerService:

    def __init__(self):
        self.dynamo_helper = DynamoDBService(table_name=AnswerTable.TABLE_NAME)

    def get_answer_by_id(self, answer_id):
        response = self.dynamo_helper.get_item(key={AnswerTable.ANSWER_ID: answer_id})
        return response

    def get_answer_by_candidate_question(self, candidate_id, question_id):
        response = self.dynamo_helper.get_item(
            index=AnswerTable.CANDIDATE_INDEX,
            key={AnswerTable.CANDIDATE_ID: candidate_id, AnswerTable.QUESTION_ID: question_id})
        return response
