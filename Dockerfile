FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV FLASK_APP=app/__init__.py
ENV FLASK_ENV=production

EXPOSE 5500
CMD ["flask", "run", "--host=0.0.0.0", "--port=5500"]
