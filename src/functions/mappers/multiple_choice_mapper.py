from src.db.tables import QuestionsTable, AnswerTable, AnswerMetadataMultipleChoice, QuestionMetadataMultipleChoice


def get_candidate_question(question):
    # remove sensitive data

    return {
        QuestionsTable.QUESTION_ID: question.get(QuestionsTable.QUESTION_ID),
        QuestionsTable.QUESTION_BODY: question.get(QuestionsTable.QUESTION_BODY),
        QuestionsTable.QUESTION_NAME: question.get(QuestionsTable.QUESTION_NAME),
        QuestionsTable.QUESTION_TITLE: question.get(QuestionsTable.QUESTION_TITLE),
        QuestionsTable.QUESTION_TYPE: question.get(QuestionsTable.QUESTION_TYPE),
        QuestionsTable.METADATA: {
            QuestionMetadataMultipleChoice.CHOICES: question.get(QuestionsTable.METADATA, {}).get(
                QuestionMetadataMultipleChoice.CHOICES, [])
        }
    }


def get_answered_question(question, answer):
    question_metadata = question.get(QuestionsTable.METADATA, {})
    answer_metadata = answer.get(AnswerTable.METADATA, {})
    selected_choice = answer_metadata.get(AnswerMetadataMultipleChoice.SELECTED_CHOICE, None)
    choices = question_metadata.get(QuestionMetadataMultipleChoice.CHOICES, [])
    correct_choice = question_metadata.get(QuestionMetadataMultipleChoice.CORRECT_CHOICE, None)
    return {
        **question,
        QuestionsTable.METADATA: {
            QuestionMetadataMultipleChoice.CHOICES: choices,
            QuestionMetadataMultipleChoice.CORRECT_CHOICE: correct_choice,
            AnswerMetadataMultipleChoice.SELECTED_CHOICE: selected_choice
        },
        AnswerTable.CREATED_AT: answer.get(AnswerTable.CREATED_AT),
        AnswerTable.SCORE: 100 if selected_choice and selected_choice == correct_choice else 0
    }
