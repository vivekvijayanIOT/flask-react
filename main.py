# Vivek sample code developed for MacBook GCP
# Go ON -Checking
from flask import Flask
from flask import render_template
import logging
app = Flask(__name__)


@app.route('/')
def index():
    return "HEllo world"

@app.route('/tem')
def temp():
    return render_template('indexs.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.route('/vivek')
def second():
    return render_template('second.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port='8080',debug=False)
