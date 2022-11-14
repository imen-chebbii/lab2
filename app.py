from flask import Flask, url_for
import math
#the function to be integrated:
def f(x):

  m=abs(math.sin(x))

  return m
 
#define a function to do integration of f(x) btw. a and b:
def I(f, n, a, b):
    h = (b - a) / float(n)
    intgr = 0.0
    for i in range(1, int(n)):

      intgr = intgr + h * f(h*(float(i)+1/2)+a)

    return intgr


appFlask = Flask(__name__)
@appFlask.route('/numericalintegralservice/')
@appFlask.route('/numericalintegralservice/<a>/<b>')
def subject(a = 0,b=3.14):
    m=I(f,1000,float(a),float(b))
    return str(m)

appFlask.run(debug=True, port=5000)