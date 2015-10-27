from flask import Flask, request, render_template, abort, url_for
app = Flask(__name__)

@app.route("/")
def start():
    return  render_template('navbar.html')

@app.route("/test/img")
def pic():
    start = '<img src="'
    url = url_for('static', filename='logo.jpg')
    end = '">'
    return start+url+end, 200

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

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the requested page.", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
