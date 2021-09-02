from src.db.tables import QuestionsTable, AnswerTable, AnswerMetadataOpenText


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
    answer_metadata = answer.get(AnswerTable.METADATA, {})
    return {
        **question,
        QuestionsTable.METADATA: {
            **answer_metadata
        },
        AnswerTable.CREATED_AT: answer.get(AnswerTable.CREATED_AT),
        AnswerTable.SCORE: None
    }
