from flask import Flask, render_template, url_for
import os



app = Flask(__name__)

@app.route("/")
def mainroute():
    return render_template('Dials.html')

port=os.getenv('PORT') or 80

app.run(host='0.0.0.0', port=port)