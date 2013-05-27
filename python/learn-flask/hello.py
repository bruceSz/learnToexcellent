from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id,the id is an integer
    return 'Post %d' %post_id

@app.route("/hello")
def hello():
    return "hello world"

@app.route("/projects")
def projects():
    return "the project page"

@app.route('/about')
def about():
    return "this is made by bruceSz"

@app.route('/index')
def index():
    return "index page !"

if __name__ == "__main__":
    app.debug = True
    app.run()
