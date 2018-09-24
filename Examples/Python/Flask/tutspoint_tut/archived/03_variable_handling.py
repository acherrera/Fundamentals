"""
Purpose: learning the flask application framework
"""

from flask import Flask
app = Flask(__name__)

# Pass variable into function
@app.route('/hello<name>')
def hello_world(name):
    return 'hello {}'.format(name)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number: {}'.format(postID)

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number: {}'.format(revNo)

@app.route('/flask')
def hello_flask():
    return 'Hello Flask'

@app.route('/python/')
def hello_python():
    return 'Hello Python'



if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug = True)
