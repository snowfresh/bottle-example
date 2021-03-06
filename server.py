import bottle
import random

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Hello</p>'
  
@APP.route('/hello')
def index():
  bottle.response.content_type = 'text/html'
  return bottle.static_file('index.html', '.')
  
@APP.route('/greet/<salutation>/<name>')
def greet(salutation, name):
  return 'Hello %s %s' % (salutation, name)

if __name__ == '__main__':
  bottle.run(application=APP)
