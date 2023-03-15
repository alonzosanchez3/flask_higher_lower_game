from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
  return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph.</p>' \
    '<img src="https://media.giphy.com/media/dX8PxV3YrA87tVFFdQ/giphy.gif">'

@app.route('/bye')
def bye():
  return "Bye!"

@app.route('/username/<name>')
def greet(name):
  return f'Hello there, {name}'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=4000)
