
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Method used: {}'.format(request.method)

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good<h2>'

@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hey, there {}<h2>".format(username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2> Post ID is {} <h2>".format(post_id)

if __name__ == "__main__":
    app.run(debug=True)
