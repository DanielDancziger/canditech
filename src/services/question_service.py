from src.db.dynamo_helper import DynamoDBService
from src.db.tables import QuestionsTable


class QuestionService:

    def __init__(self):
        self.dynamo_helper = DynamoDBService(table_name=QuestionsTable.TABLE_NAME)

    def get_question_by_id(self, question_id):
        response = self.dynamo_helper.get_item(key={QuestionsTable.QUESTION_ID: question_id})
        return response

    def get_questions(self):
        response = self.dynamo_helper.get_scan_items()
        return response
