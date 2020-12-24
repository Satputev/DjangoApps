from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/main/')

def main():
    return render_template('main.html')
@app.route('/welcome/')

def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run()
