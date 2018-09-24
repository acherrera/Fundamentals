"""
Purpose: learning the flask application framework
"""

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'hello world'

# This is same as decorator above
# app.add_url_rule ('/', 'hello', hello_world)


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug = True)
