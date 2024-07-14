from os import environ

from app import app

if __name__ == "__main__":

    SERVER_HOST = environ.get("SERVER_HOST", "localhost")
    app.run(host=SERVER_HOST, port=5500, debug=False, threaded=True)
