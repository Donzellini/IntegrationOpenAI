from flask_restx import Namespace, fields

api = Namespace(
    "E-commerce OpenAI", description="API de integração com OpenAI para assistência de vendas."
)


class ResponseQuestionAnswer:
    question_post_model = api.model("QuestionModel", {"question": fields.String})

    question_post_response_model = api.model("QuestionResponseModel", {"response": fields.String})
