from flask import Flask, render_template

app = Flask(__name__)
fonte = 'https://github.com/GiornialPro/legal/blob/main/'


@app.route('/')
def casa():

    user = 'Adaylson Dias, Eng.'

    return render_template( f'{fonte}home.html' , user = user)

if __name__ == "__main__":
    app.run( port='10000', host = '0.0.0.0' )
