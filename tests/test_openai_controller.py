def test_question_and_answer(client, mock_openai_service):
    response = client.post(
        "/api/ecommerce/v1/question-and-answer",
        json={"question": "Quais são os melhores produtos para cachorros?"},
    )

    assert response.status_code == 201
    data = response.get_json()

    expected_response = {
        "response": {
            "id": "cmpl-5b4e9NQBkA",
            "object": "text_completion",
            "created": 1589478378,
            "model": "gpt-3.5-turbo",
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": "Resposta Simulada"},
                    "finish_reason": "stop",
                }
            ],
        }
    }

    assert data["response"] == expected_response["response"]["choices"][0]["message"]["content"]
