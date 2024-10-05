import logging
from flask import Flask

app = Flask(__name__)

# Update the path to ensure it's correct and doesn't conflict with any directory
logging.basicConfig(filename='/app/app.log', level=logging.INFO)

@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
