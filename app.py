from flask import Flask
from views import pages

app = Flask(__name__)

app.register_blueprint(pages, url_prefix="/pages")


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0',port=9000)
