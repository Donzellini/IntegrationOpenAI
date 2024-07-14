from flask import request
from flask_restx import Resource

from app.main.openai.openai_response_models import ResponseQuestionAnswer, api
from app.main.openai.openai_service import OpenAiService

post_response = ResponseQuestionAnswer()


@api.route("question-and-answer")
class FeedbackPostController(Resource):
    @api.expect(post_response.question_post_model)
    @api.marshal_with(post_response.question_post_response_model, code=200)
    def post(self):
        question = request.json
        feedbacks_classifieds = OpenAiService.analyze_question(question)
        return feedbacks_classifieds, 201
