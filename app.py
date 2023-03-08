from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello_World():
  return "<p>Hello World!</p>"

if __name__=="__main__":
  app.run(host='0.0.0.0', debug = True)