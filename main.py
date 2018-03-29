from flask import Flask, request
from lccaesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

encrypted_text = ''
form = """
<!doctype html> 
<html>
     <head>
        <title>Web Caesar</title>
    </head>
        <h1>Hey!</h1>
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
         <form method= "POST" action="/encrypt">
                <textarea name = "text"> </textarea>
            <label>Rotate by:
                <input type = "text" name = "rot" value=0>
            </label>
                <input type="submit">
            <p> Your encoded message is: """ + encrypted_text + """
        </form>
    <body>
</html>
        """


@app.route("/encrypt", methods= ['POST'])
def encrypt():
    movement_number = int(request.form['rot']) 
    final_text = request.form['text']
    encrypted_text = rotate_string(final_text, movement_number)
    print('rot')
    print('text')
    return "<h1>" + encrypted_text + "</h1>"

@app.route("/")
def index():
 
    return form

app.run()
