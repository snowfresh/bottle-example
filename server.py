import bottle
import random

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Hello</p>'
  
@APP.route('/hello')
def myjunk():
  return random.randint(0, 10)

if __name__ == '__main__':
  bottle.run(application=APP)
