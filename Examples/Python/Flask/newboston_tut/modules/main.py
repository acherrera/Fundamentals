
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Method used: {}'.format(request.method)


# Allows both get and post
@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"


if __name__ == "__main__":
    app.run(debug=True)
