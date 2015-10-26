from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def start():
    return  render_template('header.html')


@app.route("/account/", methods=['POST','GET'])
def account():
    if request.method == 'POST':
        print request.form
        name = request.form['name']
        return "M@N says HELLO to %s" %name
    else:
        page = '''
        <html><body>
            <form action="" method="post" name="form">
                <label for="name">Name: </label>
                <input type="text" name="name" id="name"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
        </body></html>'''

    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
