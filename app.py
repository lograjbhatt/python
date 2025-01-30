from flask import Flask

app=Flask(__name__)

@app.route('/')

def webout():

 return '<h1>DevOps is fun.test change one more time a</h1> <br> Dont mind'

app.run(host='0.0.0.0',port=7000)
