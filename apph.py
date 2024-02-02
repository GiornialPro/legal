from flask import Flask

app = Flask(__name__)

@app.route('/')
def casa():

    return 'Ola mundo, de Angola'

if __name__ == "__main__":
    app.run()