from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/" method="post" />
        <label for="rot">Rotate by:</label>
        <input id="rot" type="text" name="rot" value="0" />
        <textarea name="text"></textarea>
        <input type="submit" />
      </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    entered_rot = int(request.form['rot'])
    entered_text = request.form['text']
    encrypted = rotate_string(entered_text, entered_rot)
    return '<h1>' + encrypted + '</h1>'


app.run()