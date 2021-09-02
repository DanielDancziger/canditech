from src.db.tables import QuestionTypes, QuestionsTable, AnswerTable

from src.functions.mappers.open_text import get_candidate_question as get_candidate_question_open_text,\
    get_answered_question as get_answered_question_open_text
from src.functions.mappers.multiple_choice_mapper import get_candidate_question as \
    get_candidate_question_multiple_choice, get_answered_question as get_answered_question_multiple_choice
from src.functions.mappers.value_mapper import get_candidate_question as get_candidate_question_value, \
    get_answered_question as get_answered_question_value

from src.services.answer_service import AnswerService
from src.services.question_service import QuestionService


class HandlersView:

    def __init__(self):
        self.question_service = QuestionService()
        self.answer_service = AnswerService()

    def get_candidate_question(self, question_id):
        question = self.question_service.get_question_by_id(question_id=question_id)
        if QuestionTypes.VALUE == question.get(QuestionsTable.QUESTION_TYPE):
            return get_candidate_question_value(question=question)
        elif QuestionTypes.MULTIPLE_CHOICE == question.get(QuestionsTable.QUESTION_TYPE):
            return get_candidate_question_multiple_choice(question=question)
        else:
            return get_candidate_question_open_text(question=question)

    def get_question_review(self, question_id):
        return self.question_service.get_question_by_id(question_id=question_id)

    def get_answered_question(self, answer_id=None, candidate_id=None, question_id=None):
        if not answer_id or not (candidate_id and question_id):
            raise Exception("Missing relevant parameters AnswerId or CandidateId+QuestionId")
        if answer_id:
            answer_row = self.answer_service.get_answer_by_id(answer_id=answer_id)
            question_id = answer_row.get(AnswerTable.QUESTION_ID, None)
        else:
            answer_row = self.answer_service.get_answer_by_candidate_question(candidate_id=candidate_id,
                                                                              question_id=question_id)

        question_row = self.question_service.get_question_by_id(question_id=question_id)
        if QuestionTypes.VALUE == question_row.get(QuestionsTable.QUESTION_TYPE):
            return get_answered_question_value(answer=answer_row, question=question_row)
        elif QuestionTypes.MULTIPLE_CHOICE == question_row.get(QuestionsTable.QUESTION_TYPE):
            return get_answered_question_multiple_choice(answer=answer_row, question=question_row)
        else:
            return get_answered_question_open_text(question=question_row, answer=answer_row)







