from flask import Flask, render_template

from crudhrs import Sistema

app = Flask(__name__)

app.config.from_mapping(secret_key='merdatoda222', DEBUG=True)
app.config["SESSION_PERMANET"] = False

@app.route('/', methods=['POST','GET'] )
def casa():

    Sistema('UNIDADE.xlsx').addciona()

    user = 'Adaylson Dias, Eng.'
    data = Sistema('UNIDADE.xlsx').origina()

    return render_template( 'home.html' , user = user, data=data)

if __name__ == "__main__":
    app.run( port='10000', host = '0.0.0.0' )
