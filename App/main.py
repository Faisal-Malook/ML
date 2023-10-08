from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello! My name is Mahek Kathiriya and my Student ID is s2231752.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
