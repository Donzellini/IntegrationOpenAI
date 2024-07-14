from openai import OpenAI

from config import OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)


class OpenAiService:

    @staticmethod
    def analyze_question(question):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente especializado em vendas de produtos para animais de estimação.",
                },
                {
                    "role": "user",
                    "content": (
                        f"Analise a seguinte pergunta recebida do usuário e forneça uma resposta apropriada, "
                        f"contendo indicações de produtos disponíveis no mercado: {question}"
                    ),
                },
            ],
            max_tokens=150,
        )

        response = {"response": f"{response.choices[0].message.content.strip()}"}
        return response
