import os
from flask import Flask, render_template
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

@app.route('/')
def index():
    # Run the dinosaur game script as a subprocess
    subprocess.Popen(['python', 'dinosaur_game.py'])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
