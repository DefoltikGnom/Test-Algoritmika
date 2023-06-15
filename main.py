
from flask import Flask, rendeer_template, url_for
import os

def geine():
    return render_template('geine.html')

 folder = os.getcwd()
 app = Flask(__name__, template_folder=folder, static_folder=folder)

app.add_utl_rule('/', 'geine', geine)

app.run()
