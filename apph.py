from flask import Flask, render_template

from crudhrs import Sistema

app = Flask(__name__)

@app.route('/')
def casa():

    Sistema().addciona()

    user = 'Adaylson Dias, Eng.'
    data = Sistema().origina()

    return render_template( 'home.html' , user = user, data=data)

if __name__ == "__main__":
    app.run( port='10000', host = '0.0.0.0' )
