from unittest.mock import patch

import pytest

from app import app


class MockChatCompletionResponse:
    def __init__(self):
        self.id = "cmpl-5b4e9NQBkA"
        self.object = "text_completion"
        self.created = 1589478378
        self.model = "gpt-3.5-turbo"
        self.choices = [self.MockChoice()]
        self.usage = {"prompt_tokens": 9, "completion_tokens": 11, "total_tokens": 20}

    class MockChoice:
        def __init__(self):
            self.index = 0
            self.message = self.MockMessage()
            self.finish_reason = "stop"

        class MockMessage:

            def __init__(self):
                self.role = "assistant"
                self.content = "Resposta Simulada"


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def mock_openai_key(monkeypatch):
    monkeypatch.setenv("OPENAI_KEY", "mock_openai_key")


@pytest.fixture
def mock_openai_service():
    with patch("app.main.openai.openai_service.client.chat.completions.create") as mock_create:
        mock_response = MockChatCompletionResponse()
        mock_create.return_value = mock_response
        yield mock_create
