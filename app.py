from markupsafe import escape
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'
@app.route('/url_for')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='gray'))
    print(url_for('user_page',name='a'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test page'