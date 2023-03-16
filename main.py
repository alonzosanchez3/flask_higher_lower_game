from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/bye')
def bye():
  return "Bye!"

@app.route('/username/<name>')
def greet(name):
  return f'Hello, {name}'

if __name__ == '__main__':
  app.run()
