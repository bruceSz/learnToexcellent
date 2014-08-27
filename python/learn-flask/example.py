from flask import Flask

app = Flask(__name__)

@app.route('/',defaults={'name':'Guest'})
@app.route('/<string:name>',methods=['GET'])
def say_hello(name):
    return 'Hello'+name

if __name__ == '__main__':
    app.run(debug=True)
