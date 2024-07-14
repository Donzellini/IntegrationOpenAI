from flask import Blueprint, Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.main.openai.openai_controller import api as feedback_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

blueprint = Blueprint("api", __name__)
app.register_blueprint(blueprint)

api = Api(
    app,
    title="API Ecommerce Open AI",
    version="1.0",
    description="API de integração com OpenAI para assistência de vendas.",
    prefix="/api/ecommerce/v1",
)

api.add_namespace(feedback_ns, path="/")
