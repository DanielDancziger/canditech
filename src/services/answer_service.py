from src.db.dynamo_helper import DynamoDBService
from src.db.tables import AnswerTable


class AnswerService:

    def __init__(self):
        self.dynamo_helper = DynamoDBService(table_name=AnswerTable.TABLE_NAME)

    def get_answer_by_id(self, answer_id):
        key = [{"key": AnswerTable.ANSWER_ID, "values": answer_id}]
        params = self.dynamo_helper.get_params(
            key_filters=key)
        response = self.dynamo_helper.query_items(params=params)
        return response[0] if response else {}

    def get_answer_by_candidate_question(self, candidate_id, question_id):
        key = [{"key": AnswerTable.CANDIDATE_ID, "values": candidate_id},
               {"key": AnswerTable.QUESTION_ID, "values": question_id}]
        params = self.dynamo_helper.get_params(key_filters=key,
                                               index_name=AnswerTable.CANDIDATE_INDEX)
        response = self.dynamo_helper.query_items(params=params)
        return response[0] if response else {}

    def get_answers_by_candidate(self, candidate_id):
        key = [{"key": AnswerTable.CANDIDATE_ID, "values": candidate_id}]
        params = self.dynamo_helper.get_params(key_filters=key,
                                               index_name=AnswerTable.CANDIDATE_INDEX)
        response = self.dynamo_helper.query_items(params=params)
        return response if response else []

