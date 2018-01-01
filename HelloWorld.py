from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

if __name__=="__main__":
    app.run(10.200.1.92:5000)
