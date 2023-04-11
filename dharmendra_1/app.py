from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_game')
def run_game():
    output = subprocess.check_output(['python', 'treasure_hunt.py'])
    return output

if __name__ == '__main__':
    app.run(debug=True)
