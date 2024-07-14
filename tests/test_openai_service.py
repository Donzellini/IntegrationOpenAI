import unittest
from unittest.mock import patch

from app.main.openai.openai_service import OpenAiService


class TestOpenAiService(unittest.TestCase):

    @patch("app.main.openai.openai_service.client.chat.completions.create")
    def test_analyze_question(self, mock_openai_service):
        # mock_response = {
        #     'choices': [{
        #         'message': {
        #             'content': 'Resposta simulada'
        #         }
        #     }]
        # }
        # mock_create.return_value = mock_response

        question = "Quais são os melhores produtos para cachorros?"
        response = OpenAiService.analyze_question(question)

        assert "response" in response
