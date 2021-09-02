from src.db.tables import QuestionsTable, AnswerTable, QuestionMetadataValue, AnswerMetadataValue


def get_candidate_question(question):
    # remove sensitive data

    return {
        QuestionsTable.QUESTION_ID: question.get(QuestionsTable.QUESTION_ID),
        QuestionsTable.QUESTION_BODY: question.get(QuestionsTable.QUESTION_BODY),
        QuestionsTable.QUESTION_NAME: question.get(QuestionsTable.QUESTION_NAME),
        QuestionsTable.QUESTION_TITLE: question.get(QuestionsTable.QUESTION_TITLE),
        QuestionsTable.QUESTION_TYPE: question.get(QuestionsTable.QUESTION_TYPE),
        QuestionsTable.METADATA: {
        }
    }


def get_answered_question(question, answer):
    question_metadata = question.get(QuestionsTable.METADATA, {})
    answer_metadata = answer.get(AnswerTable.METADATA, {})
    correct_value = question_metadata.get(QuestionMetadataValue.CORRECT_VALUE, None)
    value = answer_metadata.get(AnswerMetadataValue.VALUE, None)
    return {
        **question,
        QuestionsTable.METADATA: {
            QuestionMetadataValue.CORRECT_VALUE: correct_value,
            AnswerMetadataValue.VALUE: value
        },
        AnswerTable.CREATED_AT: answer.get(AnswerTable.CREATED_AT),
        AnswerTable.SCORE: 100 if value and value == correct_value else 0
    }
