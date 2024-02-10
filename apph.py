from flask import Flask, render_template

app = Flask(__name__)

from flask import Flask, render_template

from crudhrs import Sistema

app = Flask(__name__)

@app.route('/')
def casa():

    Sistema().origina()

    user = 'Adaylson Dias, Eng.'

    return render_template( 'home.html' , user = user)

if __name__ == "__main__":
    app.run( port='10000', host = '0.0.0.0' )
