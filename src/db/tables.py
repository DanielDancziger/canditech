import os

env = os.getenv('ENV', 'dev')
service_name = os.getenv('SERVICE_NAME', 'canditech')


class QuestionsTable:
    TABLE_NAME = os.getenv('QUESTIONS_TABLE', f'{service_name}-{env}-questions_table')
    QUESTION_ID = "questionId"
    QUESTION_NAME = "questionName"
    QUESTION_TITLE = "questionTitle"
    QUESTION_BODY = "questionBody"
    QUESTION_TYPE = "questionType"
    METADATA = "metadata"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"


class QuestionTypes:
    OPEN_TEXT = 'openText'
    CODE = 'code'
    MULTIPLE_CHOICE = 'multipleChoice'
    ONE_CHOICE = 'oneChoice'
    VIDEO = 'video'
    VALUE = 'value'


class AnswerTable:
    TABLE_NAME = os.getenv('ANSWERS_TABLE', f'{service_name}-{env}-answers_table')
    CANDIDATE_INDEX = os.getenv('CANDIDATE_INDEX', f'CandidateQuestionIndex')
    ANSWER_ID = "answerId"
    METADATA = "metadata"
    QUESTION_TYPE = "questionType"
    QUESTION_ID = "questionId"
    CREATED_AT = "createdAt"
    CANDIDATE_ID = "candidateId"
    COMPANY_ID = "companyId"
    POSITION_ID = "positionId",
    SCORE = "score"


class QuestionMetadataVideo:
    pass


class QuestionMetadataMultipleChoice:
    CHOICES = "choices"
    CORRECT_CHOICE = "correctChoice"


class QuestionMetadataValue:
    CORRECT_VALUE = "correctValue"


class AnswerMetadataVideo:
    VIDEO_URL = "videoUrl"


class AnswerMetadataMultipleChoice:
    SELECTED_CHOICE = "selectedChoice"


class AnswerMetadataOpenText:
    TEXT = "text"


class AnswerMetadataValue:
    VALUE = "value"
