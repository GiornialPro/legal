from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def casa():

    user = 'Adaylson Dias, Eng.'

    return render_template('home.html', user = user)

if __name__ == "__main__":
    app.run( port='10000', host = '0.0.0.0' )
